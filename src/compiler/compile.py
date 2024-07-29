import codecs
from typing import Generator, List, Tuple, Union

from protos.celaut_pb2 import Any

from src.utils import logger as l
import json
import os, subprocess
import src.manager.resources_manager as resources_manager
from grpcbigbuffer import client as grpcbb
from grpcbigbuffer import buffer_pb2, block_builder
from protos import celaut_pb2 as celaut, compile_pb2, gateway_pb2_grpcbf
from src.utils.env import COMPILER_SUPPORTED_ARCHITECTURES, CACHE, COMPILER_MEMORY_SIZE_FACTOR, DOCKER_COMMAND, \
    SAVE_ALL, \
    MIN_BUFFER_BLOCK_SIZE, SHA3_256_ID
from src.utils.utils import get_service_hex_main_hash
from src.utils.verify import get_service_list_of_hashes, calculate_hashes, calculate_hashes_by_stream


class Compiler:
    def __init__(self, path, aux_id):
        super().__init__()
        self.blocks: List[bytes] = []
        self.service = compile_pb2.Service()
        self.metadata = celaut.Any.Metadata()
        self.path = path
        self.json = json.load(open(self.path + "service.json", "r"))
        self.aux_id = aux_id

        arch = None
        for a in COMPILER_SUPPORTED_ARCHITECTURES:
            if self.json.get('architecture') in a: arch = a[0]

        if not arch: raise Exception("Can't compile this service, not supported architecture.")

        # Directories are created on cache.
        os.system("mkdir " + CACHE + self.aux_id + "/building")
        os.system("mkdir " + CACHE + self.aux_id + "/filesystem")

        l.LOGGER(f"Arch selected {arch}")

        # Build container and get compressed layers.
        if not os.path.isfile(self.path + 'Dockerfile'): raise Exception("Error: Dockerfile no encontrado.")
        os.system(
            DOCKER_COMMAND + ' buildx build --platform ' + arch + ' --no-cache -t builder' + self.aux_id + ' ' + self.path)
        os.system(
            DOCKER_COMMAND + " save builder" + self.aux_id + " > " + CACHE + self.aux_id + "/building/container.tar")
        os.system(
            "tar -xvf " + CACHE + self.aux_id + "/building/container.tar -C " + CACHE + self.aux_id + "/building/")

        self.buffer_len = int(
            subprocess.check_output([DOCKER_COMMAND + " image inspect builder" + aux_id + " --format='{{.Size}}'"],
                                    shell=True))

    def parseContainer(self):
        def parseFilesys() -> celaut.Any.Metadata.HashTag:
            # Save his filesystem on cache.
            for layer in os.listdir(CACHE + self.aux_id + "/building/"):
                if os.path.isdir(CACHE + self.aux_id + "/building/" + layer):
                    l.LOGGER('Unzipping layer ' + layer)
                    os.system(
                        "tar -xvf " + CACHE + self.aux_id + "/building/" + layer + "/layer.tar -C "
                        + CACHE + self.aux_id + "/filesystem/"
                    )

            # Add filesystem data to filesystem buffer object.
            def recursive_parsing(directory: str) -> celaut.Service.Container.Filesystem:
                host_dir = CACHE + self.aux_id + "/filesystem"
                filesystem = celaut.Service.Container.Filesystem()
                for b_name in os.listdir(host_dir + directory):
                    if b_name == '.wh..wh..opq':
                        # https://github.com/opencontainers/image-spec/blob/master/layer.md#opaque-whiteout
                        continue
                    branch = celaut.Service.Container.Filesystem.ItemBranch()
                    branch.name = os.path.basename(b_name)

                    # It's a link.
                    if os.path.islink(host_dir + directory + b_name):
                        branch.link.dst = directory + b_name
                        branch.link.src = os.path.realpath(host_dir + directory + b_name)[
                                          len(host_dir):] if host_dir in os.path.realpath(
                            host_dir + directory + b_name) else os.path.realpath(host_dir + directory + b_name)

                    # It's a file.
                    elif os.path.isfile(host_dir + directory + b_name):
                        if os.path.getsize(host_dir + directory + b_name) < MIN_BUFFER_BLOCK_SIZE:
                            with open(host_dir + directory + b_name, 'rb') as file:
                                branch.file = file.read()

                        else:
                            block_hash, block = block_builder.create_block(
                                file_path=host_dir + directory + b_name,
                                copy=True
                            )
                            branch.file = block.SerializeToString()
                            if block_hash not in self.blocks:
                                self.blocks.append(block_hash)

                    # It's a folder.
                    elif os.path.isdir(host_dir + directory + b_name):
                        branch.filesystem.CopyFrom(
                            recursive_parsing(directory=directory + b_name + '/')
                        )

                    filesystem.branch.append(branch)

                return filesystem

            self.service.container.filesystem.CopyFrom(recursive_parsing(directory="/"))

            return celaut.Any.Metadata.HashTag(
                hash=calculate_hashes(
                    value=self.service.container.filesystem.SerializeToString()
                ) if not self.blocks else
                calculate_hashes_by_stream(
                    value=grpcbb.read_multiblock_directory(
                        directory=block_builder.build_multiblock(
                            pf_object_with_block_pointers=self.service.container.filesystem,
                            blocks=self.blocks
                        )[1],
                        delete_directory=True,
                        ignore_blocks=True
                    )
                )
            )

        # Envs
        if self.json.get('envs'):
            for env in self.json.get('envs'):
                try:
                    with open(self.path + env + ".field", "rb") as env_desc:
                        self.service.container.enviroment_variables[env].ParseFromString(env_desc.read())
                except FileNotFoundError:
                    pass

        # Entrypoint
        if self.json.get('entrypoint'):
            self.service.container.entrypoint.append(self.json.get('entrypoint'))

        # Arch

        # Config file spec.
        self.service.container.config.path.append('__config__')
        self.service.container.config.format.CopyFrom(
            celaut.FieldDef()  # celaut.ConfigFile definition.
        )

        # Expected Gateway.

        # Add container metadata to the global metadata.
        self.metadata.hashtag.attr_hashtag.append(
            celaut.Any.Metadata.HashTag.AttrHashTag(
                key=1,  # Container attr.
                value=[
                    celaut.Any.Metadata.HashTag(
                        attr_hashtag=[
                            celaut.Any.Metadata.HashTag.AttrHashTag(
                                key=1,  # Architecture
                                value=[
                                    celaut.Any.Metadata.HashTag(
                                        tag=[
                                            self.json.get('architecture')
                                        ]
                                    )
                                ]
                            ),
                            celaut.Any.Metadata.HashTag.AttrHashTag(
                                key=2,  # Filesystem
                                value=[parseFilesys()]
                            )
                        ]
                    )
                ]
            )
        )

    def parseApi(self):
        #  App protocol
        try:
            with open(self.path + "api.application", "rb") as api_desc:
                self.service.api.app_protocol.ParseFromString(api_desc.read())
        except:
            pass

        #  Slots 
        if not self.json.get('api'): return
        for item in self.json.get('api'):  # iterate slots.
            slot = celaut.Service.Api.Slot()
            # port.
            slot.port = item.get('port')
            #  transport protocol.
            #  TODO: slot.transport_protocol = Protocol()
            self.service.api.slot.append(slot)

        # Add api metadata to the global metadata.
        self.metadata.hashtag.attr_hashtag.append(
            celaut.Any.Metadata.HashTag.AttrHashTag(
                key=2,  # Api attr.
                value=[
                    celaut.Any.Metadata.HashTag(
                        attr_hashtag=[
                            celaut.Any.Metadata.HashTag.AttrHashTag(
                                key=2,  # Slot attr.
                                value=[
                                    celaut.Any.Metadata.HashTag(
                                        attr_hashtag=[
                                            celaut.Any.Metadata.HashTag.AttrHashTag(
                                                key=2,  # Transport Protocol attr.
                                                value=[
                                                    celaut.Any.Metadata.HashTag(
                                                        tag=item.get('protocol')
                                                    )
                                                ]
                                            )
                                        ]
                                    ) for item in self.json.get('api')
                                ]
                            )
                        ]
                    )
                ]
            )
        )

    def parseLedger(self):
        #  TODO: self.service.ledger.

        #  Add ledger metadata to the global metadata.
        if self.json.get('ledger'):
            self.metadata.hashtag.attr_hashtag.append(
                celaut.Any.Metadata.HashTag.AttrHashTag(
                    key=4,  # Ledger attr.
                    value=(
                        celaut.Any.MetaData.HashTag(
                            tag=self.json.get('ledger')
                        )
                    )
                )
            )

    def parseTensor(self):
        tensor = self.json.get('tensor') or None
        if tensor:
            self.service.tensor.rank = tensor["rank"] or None
            indexes = tensor.get('index') or None
            if indexes:
                for var in indexes:
                    try:
                        with open(self.path + var + ".field", "rb") as var_desc:
                            self.service.tensor.index[var].ParseFromString(var_desc.read())
                    except FileNotFoundError:
                        pass

                # Add tensor metadata to the global metadata.
                self.metadata.hashtag.attr_hashtag.append(
                    celaut.Any.Metadata.HashTag.AttrHashTag(
                        key=3,  # Tensor attr.
                        value=[
                            celaut.Any.Metadata.HashTag(
                                attr_hashtag=[
                                    celaut.Any.Metadata.HashTag.AttrHashTag(
                                        key=1,  # index attr.
                                        value=[
                                            celaut.Any.Metadata.HashTag(
                                                tag=indexes[var]
                                            ) for var in indexes
                                        ]
                                    )
                                ]
                            ),
                        ]
                    )
                )

    def save(self) -> Tuple[str, celaut.Any.Metadata, Union[str, compile_pb2.Service]]:
        service: Union[str, compile_pb2.Service]
        if not self.blocks:
            service_buffer = self.service.SerializeToString()  # 2*len
            self.metadata.hashtag.hash.extend(
                get_service_list_of_hashes(
                    service_buffer=service_buffer
                )
            )
            service_id: str = get_service_hex_main_hash(
                metadata=self.metadata
            )

            # Once service hashes are calculated, we prune the filesystem for save storage.
            # self.service.container.filesystem.ClearField('branch')
            # https://github.com/moby/moby/issues/20972#issuecomment-193381422
            del service_buffer  # -len

            service = self.service

        else:
            # Generate the hashes.
            bytes_id, service_directory = block_builder.build_multiblock(
                pf_object_with_block_pointers=self.service,
                blocks=self.blocks
            )
            service_id: str = codecs.encode(bytes_id, 'hex').decode('utf-8')

            self.metadata.hashtag.hash.extend(
                [Any.Metadata.HashTag.Hash(
                    type=SHA3_256_ID,
                    value=bytes_id
                )]
            )

            from hashlib import sha3_256
            validate_content = sha3_256()
            for i in grpcbb.read_multiblock_directory(directory=service_directory):
                validate_content.update(i)

            print(f'\n\nCONTENT ID -> {service_id}')
            print(f'\n\nCONTENT VALIDATED ID -> {validate_content.hexdigest()}')

            service = service_directory

        return service_id, self.metadata, service


def ok(path, aux_id) -> Tuple[str, celaut.Any.Metadata, Union[str, compile_pb2.Service]]:
    spec_file = Compiler(path=path, aux_id=aux_id)

    with resources_manager.mem_manager(len=COMPILER_MEMORY_SIZE_FACTOR * spec_file.buffer_len):
        spec_file.parseContainer()
        spec_file.parseApi()
        spec_file.parseLedger()
        spec_file.parseTensor()

        identifier, metadata, service = spec_file.save()

    # os.system(DOCKER_COMMAND+' tag builder' + aux_id + ' ' + identifier + '.docker')
    os.system(DOCKER_COMMAND + ' rmi builder' + aux_id)
    os.system('rm -rf ' + CACHE + aux_id + '/')
    return identifier, metadata, service


def zipfile_ok(
        zip: str
) -> Tuple[str, celaut.Any.Metadata, Union[str, compile_pb2.Service]]:
    import random
    aux_id = str(random.random())
    os.system('mkdir ' + CACHE + aux_id)
    os.system('mkdir ' + CACHE + aux_id + '/for_build')
    os.system('unzip ' + zip + ' -d ' + CACHE + aux_id + '/for_build')
    os.system('rm ' + zip)
    return ok(
        path=CACHE + aux_id + '/for_build/',
        aux_id=aux_id,
    )  # Specification file


def compile_zip( zip, saveit: bool = SAVE_ALL) -> Generator[buffer_pb2.Buffer, None, None]:
    l.LOGGER('Compiling zip ' + str(zip))
    service_id, metadata, service = zipfile_ok(zip=zip)
    for b in grpcbb.serialize_to_buffer(
            message_iterator=[
                compile_pb2.CompileOutputServiceId(
                    id=bytes.fromhex(service_id)
                ),
                metadata,
                grpcbb.Dir(dir=service, _type=compile_pb2.Service)
                if type(service) is str else service
            ],
            indices=gateway_pb2_grpcbf.CompileOutput_indices
    ):
        yield b

    # shutil.rmtree(service_with_meta.name)
    # TODO if saveit: convert dirs to local partition model and save it into the registry.


"""
if __name__ == "__main__":
    from protos.gateway_pb2_grpcbf import StartService_input_partitions_v1

    id = repo_ok(
        repo=sys.argv[1],
        partitions_model=StartService_input_partitions_v1[2] if not len(sys.argv) > 1 else [
            buffer_pb2.Buffer.Head.Partition()]
    )
    os.system('mv ' + CACHE + 'compile' + id + ' ' + REGISTRY + id)
    print(id)

"""

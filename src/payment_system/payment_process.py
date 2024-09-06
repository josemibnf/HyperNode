import string
from hashlib import sha3_256
from time import sleep
import grpc
from grpcbigbuffer import client as grpcbf
from src.payment_system.ledger_balancer import ledger_balancer

from src.payment_system.contracts.envs import AVAILABLE_PAYMENT_PROCESS, PAYMENT_PROCESS_VALIDATORS

from protos import gateway_pb2_grpc, gateway_pb2

from src.manager.manager import get_client_id_on_other_peer, increase_local_gas_for_client
from src.database.sql_connection import SQLConnection

from src.utils import logger as _l
from src.utils.utils import to_gas_amount, generate_uris_by_peer_id
from src.database.access_functions.ledgers import get_peer_contract_instances
from src.utils.env import EnvManager

env_manager = EnvManager()

COMMUNICATION_ATTEMPTS = env_manager.get_env("COMMUNICATION_ATTEMPTS")
COMMUNICATION_ATTEMPTS_DELAY = env_manager.get_env("COMMUNICATION_ATTEMPTS_DELAY")
MIN_DEPOSIT_PEER = env_manager.get_env("MIN_DEPOSIT_PEER")

sc = SQLConnection()


def __peer_payment_process(peer_id: str, amount: int) -> bool:
    deposit_token: str = get_client_id_on_other_peer(peer_id=peer_id)
    _l.LOGGER('Peer payment process to peer ' + peer_id + ' with client ' + deposit_token + ' of ' + str(amount))
    for contract_hash, process_payment in AVAILABLE_PAYMENT_PROCESS.items():
        # check if the payment process is compatible with this peer.
        try:
            for contract_address, ledger in ledger_balancer(
                    ledger_generator=get_peer_contract_instances(
                        contract_hash=contract_hash,
                        peer_id=peer_id
                    )
            ):
                _l.LOGGER(
                    'Peer payment process:   Ledger: ' + str(ledger) + ' Contract address: ' + str(contract_address))
                contract_ledger = process_payment(
                    amount=amount,
                    token=deposit_token,
                    ledger=ledger,
                    contract_address=contract_address
                )
                _l.LOGGER('Peer payment process: payment process executed. Ledger: ' + str(
                    contract_ledger.ledger) + ' Contract address: ' + str(contract_ledger.contract_addr))
                attempt = 0
                while True:
                    try:
                        next(grpcbf.client_grpc(
                            method=gateway_pb2_grpc.GatewayStub(
                                grpc.insecure_channel(
                                    next(generate_uris_by_peer_id(peer_id=peer_id))
                                )
                            ).Payable,
                            partitions_message_mode_parser=True,
                            input=gateway_pb2.Payment(
                                gas_amount=to_gas_amount(amount),
                                deposit_token=deposit_token,
                                contract_ledger=contract_ledger,
                            )
                        )
                        )
                        _l.LOGGER('Peer payment process to ' + peer_id + ' of ' + str(amount) + ' communicated.')
                        break
                    except Exception as e:
                        attempt += 1
                        if attempt >= COMMUNICATION_ATTEMPTS:
                            _l.LOGGER('Peer payment communication process:   Failed. ' + str(e))
                            # TODO subtract node reputation
                            return False
                        sleep(COMMUNICATION_ATTEMPTS_DELAY)
            # TODO, aqui hay que controlar el caso en que no tengamos ningun contrato disponible para ese par.
            #  porque ahora estamos diciendo que está ok. Pero en realidad no hemos hecho nada
            #  y va a entrar en loop todo el tiempo o reducirá su reputación ....
        except Exception as e:
            _l.LOGGER('Peer payment process error: ' + str(e))
            return False
        return True
    return False


def __increase_deposit_on_peer(peer_id: str, amount: int) -> bool:
    _l.LOGGER('Increase deposit on peer ' + peer_id + ' by ' + str(amount))
    try:
        if __peer_payment_process(peer_id=peer_id, amount=amount):
            if sc.add_gas_to_peer(peer_id=peer_id, gas=amount):
                return True
            else:
                _l.LOGGER(f'Failed to add gas to peer {peer_id}')
                return False
        else:
            return False
    except Exception as e:
        _l.LOGGER(f'Error increasing deposit on peer {peer_id}: {e}')
        return False


def increase_deposit_on_peer(peer_id: str, amount: int) -> bool:
    try:
        return __increase_deposit_on_peer(peer_id=peer_id, amount=amount + MIN_DEPOSIT_PEER)
    except Exception as e:
        _l.LOGGER('Manager error: ' + str(e))
        return False


def validate_payment_process(amount: int, ledger: str, contract: bytes, contract_addr: str, token: str) -> bool:
    return __check_payment_process(amount=amount, ledger=ledger, token=token, contract=contract,
                                   contract_addr=contract_addr) \
        and increase_local_gas_for_client(client_id=token, amount=amount)  # TODO allow for containers too.


def __check_payment_process(amount: int, ledger: str, token: str, contract: bytes, contract_addr: string) -> bool:
    _l.LOGGER('Check payment process to ' + token + ' of ' + str(amount))
    if not sc.client_exists(client_id=token):
        _l.LOGGER(f"Client id {token} not in clients.")
        return False
    return PAYMENT_PROCESS_VALIDATORS[sha3_256(contract).hexdigest()](amount, token, ledger, contract_addr,
                                                                    validate_token=lambda t: sc.client_exists(client_id=t))


def init_contract_interfaces():
    pass
    # vyper_gdc.VyperDepositContractInterface()

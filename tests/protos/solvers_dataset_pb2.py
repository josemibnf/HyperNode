# -*- coding: utf-8 -*-
# Generated by the protocol buffer compilers.  DO NOT EDIT!
# source: solvers_dataset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import celaut_pb2 as celaut__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15solvers_dataset.proto\x12\x07\x64\x61taset\x1a\x0c\x63\x65laut.proto\"$\n\x04\x44\x61ta\x12\r\n\x05score\x18\x01 \x01(\x02\x12\r\n\x05index\x18\x02 \x01(\x05\"\xe9\x01\n\x10SolverWithConfig\x12\"\n\x04meta\x18\x01 \x01(\x0b\x32\x14.celaut.Any.Metadata\x12#\n\ndefinition\x18\x02 \x01(\x0b\x32\x0f.celaut.Service\x12P\n\x14\x65nviroment_variables\x18\x03 \x03(\x0b\x32\x32.dataset.SolverWithConfig.EnviromentVariablesEntry\x1a:\n\x18\x45nviromentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\x7f\n\x0f\x44\x61taSetInstance\x12\x30\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\".dataset.DataSetInstance.DataEntry\x1a:\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.dataset.Data:\x02\x38\x01\"z\n\x07\x44\x61taSet\x12(\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1a.dataset.DataSet.DataEntry\x1a\x45\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.dataset.DataSetInstance:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'solvers_dataset_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SOLVERWITHCONFIG_ENVIROMENTVARIABLESENTRY._options = None
  _SOLVERWITHCONFIG_ENVIROMENTVARIABLESENTRY._serialized_options = b'8\001'
  _DATASETINSTANCE_DATAENTRY._options = None
  _DATASETINSTANCE_DATAENTRY._serialized_options = b'8\001'
  _DATASET_DATAENTRY._options = None
  _DATASET_DATAENTRY._serialized_options = b'8\001'
  _globals['_DATA']._serialized_start=48
  _globals['_DATA']._serialized_end=84
  _globals['_SOLVERWITHCONFIG']._serialized_start=87
  _globals['_SOLVERWITHCONFIG']._serialized_end=320
  _globals['_SOLVERWITHCONFIG_ENVIROMENTVARIABLESENTRY']._serialized_start=262
  _globals['_SOLVERWITHCONFIG_ENVIROMENTVARIABLESENTRY']._serialized_end=320
  _globals['_DATASETINSTANCE']._serialized_start=322
  _globals['_DATASETINSTANCE']._serialized_end=449
  _globals['_DATASETINSTANCE_DATAENTRY']._serialized_start=391
  _globals['_DATASETINSTANCE_DATAENTRY']._serialized_end=449
  _globals['_DATASET']._serialized_start=451
  _globals['_DATASET']._serialized_end=573
  _globals['_DATASET_DATAENTRY']._serialized_start=504
  _globals['_DATASET_DATAENTRY']._serialized_end=573
# @@protoc_insertion_point(module_scope)

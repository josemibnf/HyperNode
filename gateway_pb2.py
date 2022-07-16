# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import celaut_pb2 as celaut__pb2
import buffer_pb2 as buffer__pb2
import compile_pb2 as compile__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway.proto',
  package='gateway',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rgateway.proto\x12\x07gateway\x1a\x0c\x63\x65laut.proto\x1a\x0c\x62uffer.proto\x1a\rcompile.proto\"\x1d\n\x0cTokenMessage\x12\r\n\x05token\x18\x01 \x01(\t\"/\n\rEstimatedCost\x12\x0c\n\x04\x63ost\x18\x01 \x01(\x03\x12\x10\n\x08variance\x18\x02 \x01(\x02\"\x18\n\x06Refund\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x03\"q\n\x07Payment\x12\x15\n\rdeposit_token\x18\x01 \x01(\t\x12;\n\x0f\x63ontract_ledger\x18\x03 \x01(\x0b\x32\".celaut.Service.Api.ContractLedger\x12\x12\n\ngas_amount\x18\x04 \x01(\x03\"\x1d\n\x07Metrics\x12\x12\n\ngas_amount\x18\x01 \x01(\x03\"\x90\x01\n\x08Instance\x12\x30\n\rinstance_meta\x18\x01 \x01(\x0b\x32\x14.celaut.Any.MetadataH\x00\x88\x01\x01\x12\"\n\x08instance\x18\x02 \x01(\x0b\x32\x10.celaut.Instance\x12\x12\n\x05token\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x10\n\x0e_instance_metaB\x08\n\x06_token\"[\n\x0fServiceWithMeta\x12&\n\x08metadata\x18\x01 \x01(\x0b\x32\x14.celaut.Any.Metadata\x12 \n\x07service\x18\x02 \x01(\x0b\x32\x0f.celaut.Service\"\x9c\x02\n\x0eHashWithConfig\x12/\n\x04hash\x18\x01 \x01(\x0b\x32!.celaut.Any.Metadata.HashTag.Hash\x12%\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x15.celaut.Configuration\x12-\n\nmin_sysreq\x18\x04 \x01(\x0b\x32\x14.celaut.SysresourcesH\x00\x88\x01\x01\x12-\n\nmax_sysreq\x18\x05 \x01(\x0b\x32\x14.celaut.SysresourcesH\x01\x88\x01\x01\x12\x1f\n\x12initial_gas_amount\x18\x06 \x01(\x05H\x02\x88\x01\x01\x42\r\n\x0b_min_sysreqB\r\n\x0b_max_sysreqB\x15\n\x13_initial_gas_amount\"\x99\x02\n\x11ServiceWithConfig\x12)\n\x07service\x18\x02 \x01(\x0b\x32\x18.gateway.ServiceWithMeta\x12%\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x15.celaut.Configuration\x12-\n\nmin_sysreq\x18\x04 \x01(\x0b\x32\x14.celaut.SysresourcesH\x00\x88\x01\x01\x12-\n\nmax_sysreq\x18\x05 \x01(\x0b\x32\x14.celaut.SysresourcesH\x01\x88\x01\x01\x12\x1f\n\x12initial_gas_amount\x18\x06 \x01(\x05H\x02\x88\x01\x01\x42\r\n\x0b_min_sysreqB\r\n\x0b_max_sysreqB\x15\n\x13_initial_gas_amount\"U\n\x0c\x43ompileInput\x12\x0c\n\x04repo\x18\x01 \x01(\x0c\x12\x37\n\x10partitions_model\x18\x02 \x03(\x0b\x32\x1d.buffer.Buffer.Head.Partition\"F\n\rCompileOutput\x12\n\n\x02id\x18\x01 \x01(\x0c\x12)\n\x07service\x18\x02 \x01(\x0b\x32\x18.compile.ServiceWithMeta\"w\n!ModifyServiceSystemResourcesInput\x12(\n\nmin_sysreq\x18\x01 \x01(\x0b\x32\x14.celaut.Sysresources\x12(\n\nmax_sysreq\x18\x02 \x01(\x0b\x32\x14.celaut.Sysresources2\xa9\x04\n\x07Gateway\x12\x34\n\x0cStartService\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12\x33\n\x0bStopService\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12.\n\x06Hynode\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12\x44\n\x1cModifyServiceSystemResources\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12/\n\x07GetFile\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12/\n\x07\x43ompile\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12\x35\n\rGetServiceTar\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12?\n\x17GetServiceEstimatedCost\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12/\n\x07Payable\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12\x32\n\nGetMetrics\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[celaut__pb2.DESCRIPTOR,buffer__pb2.DESCRIPTOR,compile__pb2.DESCRIPTOR,])




_TOKENMESSAGE = _descriptor.Descriptor(
  name='TokenMessage',
  full_name='gateway.TokenMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='gateway.TokenMessage.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=98,
)


_ESTIMATEDCOST = _descriptor.Descriptor(
  name='EstimatedCost',
  full_name='gateway.EstimatedCost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cost', full_name='gateway.EstimatedCost.cost', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='variance', full_name='gateway.EstimatedCost.variance', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=147,
)


_REFUND = _descriptor.Descriptor(
  name='Refund',
  full_name='gateway.Refund',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='gateway.Refund.amount', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=173,
)


_PAYMENT = _descriptor.Descriptor(
  name='Payment',
  full_name='gateway.Payment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deposit_token', full_name='gateway.Payment.deposit_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contract_ledger', full_name='gateway.Payment.contract_ledger', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas_amount', full_name='gateway.Payment.gas_amount', index=2,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=288,
)


_METRICS = _descriptor.Descriptor(
  name='Metrics',
  full_name='gateway.Metrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gas_amount', full_name='gateway.Metrics.gas_amount', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=319,
)


_INSTANCE = _descriptor.Descriptor(
  name='Instance',
  full_name='gateway.Instance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_meta', full_name='gateway.Instance.instance_meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance', full_name='gateway.Instance.instance', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='gateway.Instance.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_instance_meta', full_name='gateway.Instance._instance_meta',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_token', full_name='gateway.Instance._token',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=322,
  serialized_end=466,
)


_SERVICEWITHMETA = _descriptor.Descriptor(
  name='ServiceWithMeta',
  full_name='gateway.ServiceWithMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='gateway.ServiceWithMeta.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service', full_name='gateway.ServiceWithMeta.service', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=468,
  serialized_end=559,
)


_HASHWITHCONFIG = _descriptor.Descriptor(
  name='HashWithConfig',
  full_name='gateway.HashWithConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='gateway.HashWithConfig.hash', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='gateway.HashWithConfig.config', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_sysreq', full_name='gateway.HashWithConfig.min_sysreq', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_sysreq', full_name='gateway.HashWithConfig.max_sysreq', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial_gas_amount', full_name='gateway.HashWithConfig.initial_gas_amount', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_min_sysreq', full_name='gateway.HashWithConfig._min_sysreq',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_max_sysreq', full_name='gateway.HashWithConfig._max_sysreq',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_initial_gas_amount', full_name='gateway.HashWithConfig._initial_gas_amount',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=562,
  serialized_end=846,
)


_SERVICEWITHCONFIG = _descriptor.Descriptor(
  name='ServiceWithConfig',
  full_name='gateway.ServiceWithConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='gateway.ServiceWithConfig.service', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='gateway.ServiceWithConfig.config', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_sysreq', full_name='gateway.ServiceWithConfig.min_sysreq', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_sysreq', full_name='gateway.ServiceWithConfig.max_sysreq', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial_gas_amount', full_name='gateway.ServiceWithConfig.initial_gas_amount', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_min_sysreq', full_name='gateway.ServiceWithConfig._min_sysreq',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_max_sysreq', full_name='gateway.ServiceWithConfig._max_sysreq',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_initial_gas_amount', full_name='gateway.ServiceWithConfig._initial_gas_amount',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=849,
  serialized_end=1130,
)


_COMPILEINPUT = _descriptor.Descriptor(
  name='CompileInput',
  full_name='gateway.CompileInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='repo', full_name='gateway.CompileInput.repo', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partitions_model', full_name='gateway.CompileInput.partitions_model', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1132,
  serialized_end=1217,
)


_COMPILEOUTPUT = _descriptor.Descriptor(
  name='CompileOutput',
  full_name='gateway.CompileOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gateway.CompileOutput.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service', full_name='gateway.CompileOutput.service', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1219,
  serialized_end=1289,
)


_MODIFYSERVICESYSTEMRESOURCESINPUT = _descriptor.Descriptor(
  name='ModifyServiceSystemResourcesInput',
  full_name='gateway.ModifyServiceSystemResourcesInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_sysreq', full_name='gateway.ModifyServiceSystemResourcesInput.min_sysreq', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_sysreq', full_name='gateway.ModifyServiceSystemResourcesInput.max_sysreq', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1291,
  serialized_end=1410,
)

_PAYMENT.fields_by_name['contract_ledger'].message_type = celaut__pb2._SERVICE_API_CONTRACTLEDGER
_INSTANCE.fields_by_name['instance_meta'].message_type = celaut__pb2._ANY_METADATA
_INSTANCE.fields_by_name['instance'].message_type = celaut__pb2._INSTANCE
_INSTANCE.oneofs_by_name['_instance_meta'].fields.append(
  _INSTANCE.fields_by_name['instance_meta'])
_INSTANCE.fields_by_name['instance_meta'].containing_oneof = _INSTANCE.oneofs_by_name['_instance_meta']
_INSTANCE.oneofs_by_name['_token'].fields.append(
  _INSTANCE.fields_by_name['token'])
_INSTANCE.fields_by_name['token'].containing_oneof = _INSTANCE.oneofs_by_name['_token']
_SERVICEWITHMETA.fields_by_name['metadata'].message_type = celaut__pb2._ANY_METADATA
_SERVICEWITHMETA.fields_by_name['service'].message_type = celaut__pb2._SERVICE
_HASHWITHCONFIG.fields_by_name['hash'].message_type = celaut__pb2._ANY_METADATA_HASHTAG_HASH
_HASHWITHCONFIG.fields_by_name['config'].message_type = celaut__pb2._CONFIGURATION
_HASHWITHCONFIG.fields_by_name['min_sysreq'].message_type = celaut__pb2._SYSRESOURCES
_HASHWITHCONFIG.fields_by_name['max_sysreq'].message_type = celaut__pb2._SYSRESOURCES
_HASHWITHCONFIG.oneofs_by_name['_min_sysreq'].fields.append(
  _HASHWITHCONFIG.fields_by_name['min_sysreq'])
_HASHWITHCONFIG.fields_by_name['min_sysreq'].containing_oneof = _HASHWITHCONFIG.oneofs_by_name['_min_sysreq']
_HASHWITHCONFIG.oneofs_by_name['_max_sysreq'].fields.append(
  _HASHWITHCONFIG.fields_by_name['max_sysreq'])
_HASHWITHCONFIG.fields_by_name['max_sysreq'].containing_oneof = _HASHWITHCONFIG.oneofs_by_name['_max_sysreq']
_HASHWITHCONFIG.oneofs_by_name['_initial_gas_amount'].fields.append(
  _HASHWITHCONFIG.fields_by_name['initial_gas_amount'])
_HASHWITHCONFIG.fields_by_name['initial_gas_amount'].containing_oneof = _HASHWITHCONFIG.oneofs_by_name['_initial_gas_amount']
_SERVICEWITHCONFIG.fields_by_name['service'].message_type = _SERVICEWITHMETA
_SERVICEWITHCONFIG.fields_by_name['config'].message_type = celaut__pb2._CONFIGURATION
_SERVICEWITHCONFIG.fields_by_name['min_sysreq'].message_type = celaut__pb2._SYSRESOURCES
_SERVICEWITHCONFIG.fields_by_name['max_sysreq'].message_type = celaut__pb2._SYSRESOURCES
_SERVICEWITHCONFIG.oneofs_by_name['_min_sysreq'].fields.append(
  _SERVICEWITHCONFIG.fields_by_name['min_sysreq'])
_SERVICEWITHCONFIG.fields_by_name['min_sysreq'].containing_oneof = _SERVICEWITHCONFIG.oneofs_by_name['_min_sysreq']
_SERVICEWITHCONFIG.oneofs_by_name['_max_sysreq'].fields.append(
  _SERVICEWITHCONFIG.fields_by_name['max_sysreq'])
_SERVICEWITHCONFIG.fields_by_name['max_sysreq'].containing_oneof = _SERVICEWITHCONFIG.oneofs_by_name['_max_sysreq']
_SERVICEWITHCONFIG.oneofs_by_name['_initial_gas_amount'].fields.append(
  _SERVICEWITHCONFIG.fields_by_name['initial_gas_amount'])
_SERVICEWITHCONFIG.fields_by_name['initial_gas_amount'].containing_oneof = _SERVICEWITHCONFIG.oneofs_by_name['_initial_gas_amount']
_COMPILEINPUT.fields_by_name['partitions_model'].message_type = buffer__pb2._BUFFER_HEAD_PARTITION
_COMPILEOUTPUT.fields_by_name['service'].message_type = compile__pb2._SERVICEWITHMETA
_MODIFYSERVICESYSTEMRESOURCESINPUT.fields_by_name['min_sysreq'].message_type = celaut__pb2._SYSRESOURCES
_MODIFYSERVICESYSTEMRESOURCESINPUT.fields_by_name['max_sysreq'].message_type = celaut__pb2._SYSRESOURCES
DESCRIPTOR.message_types_by_name['TokenMessage'] = _TOKENMESSAGE
DESCRIPTOR.message_types_by_name['EstimatedCost'] = _ESTIMATEDCOST
DESCRIPTOR.message_types_by_name['Refund'] = _REFUND
DESCRIPTOR.message_types_by_name['Payment'] = _PAYMENT
DESCRIPTOR.message_types_by_name['Metrics'] = _METRICS
DESCRIPTOR.message_types_by_name['Instance'] = _INSTANCE
DESCRIPTOR.message_types_by_name['ServiceWithMeta'] = _SERVICEWITHMETA
DESCRIPTOR.message_types_by_name['HashWithConfig'] = _HASHWITHCONFIG
DESCRIPTOR.message_types_by_name['ServiceWithConfig'] = _SERVICEWITHCONFIG
DESCRIPTOR.message_types_by_name['CompileInput'] = _COMPILEINPUT
DESCRIPTOR.message_types_by_name['CompileOutput'] = _COMPILEOUTPUT
DESCRIPTOR.message_types_by_name['ModifyServiceSystemResourcesInput'] = _MODIFYSERVICESYSTEMRESOURCESINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TokenMessage = _reflection.GeneratedProtocolMessageType('TokenMessage', (_message.Message,), {
  'DESCRIPTOR' : _TOKENMESSAGE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.TokenMessage)
  })
_sym_db.RegisterMessage(TokenMessage)

EstimatedCost = _reflection.GeneratedProtocolMessageType('EstimatedCost', (_message.Message,), {
  'DESCRIPTOR' : _ESTIMATEDCOST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.EstimatedCost)
  })
_sym_db.RegisterMessage(EstimatedCost)

Refund = _reflection.GeneratedProtocolMessageType('Refund', (_message.Message,), {
  'DESCRIPTOR' : _REFUND,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.Refund)
  })
_sym_db.RegisterMessage(Refund)

Payment = _reflection.GeneratedProtocolMessageType('Payment', (_message.Message,), {
  'DESCRIPTOR' : _PAYMENT,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.Payment)
  })
_sym_db.RegisterMessage(Payment)

Metrics = _reflection.GeneratedProtocolMessageType('Metrics', (_message.Message,), {
  'DESCRIPTOR' : _METRICS,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.Metrics)
  })
_sym_db.RegisterMessage(Metrics)

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.Instance)
  })
_sym_db.RegisterMessage(Instance)

ServiceWithMeta = _reflection.GeneratedProtocolMessageType('ServiceWithMeta', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEWITHMETA,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.ServiceWithMeta)
  })
_sym_db.RegisterMessage(ServiceWithMeta)

HashWithConfig = _reflection.GeneratedProtocolMessageType('HashWithConfig', (_message.Message,), {
  'DESCRIPTOR' : _HASHWITHCONFIG,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.HashWithConfig)
  })
_sym_db.RegisterMessage(HashWithConfig)

ServiceWithConfig = _reflection.GeneratedProtocolMessageType('ServiceWithConfig', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEWITHCONFIG,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.ServiceWithConfig)
  })
_sym_db.RegisterMessage(ServiceWithConfig)

CompileInput = _reflection.GeneratedProtocolMessageType('CompileInput', (_message.Message,), {
  'DESCRIPTOR' : _COMPILEINPUT,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.CompileInput)
  })
_sym_db.RegisterMessage(CompileInput)

CompileOutput = _reflection.GeneratedProtocolMessageType('CompileOutput', (_message.Message,), {
  'DESCRIPTOR' : _COMPILEOUTPUT,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.CompileOutput)
  })
_sym_db.RegisterMessage(CompileOutput)

ModifyServiceSystemResourcesInput = _reflection.GeneratedProtocolMessageType('ModifyServiceSystemResourcesInput', (_message.Message,), {
  'DESCRIPTOR' : _MODIFYSERVICESYSTEMRESOURCESINPUT,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.ModifyServiceSystemResourcesInput)
  })
_sym_db.RegisterMessage(ModifyServiceSystemResourcesInput)



_GATEWAY = _descriptor.ServiceDescriptor(
  name='Gateway',
  full_name='gateway.Gateway',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1413,
  serialized_end=1966,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartService',
    full_name='gateway.Gateway.StartService',
    index=0,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopService',
    full_name='gateway.Gateway.StopService',
    index=1,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Hynode',
    full_name='gateway.Gateway.Hynode',
    index=2,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ModifyServiceSystemResources',
    full_name='gateway.Gateway.ModifyServiceSystemResources',
    index=3,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetFile',
    full_name='gateway.Gateway.GetFile',
    index=4,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Compile',
    full_name='gateway.Gateway.Compile',
    index=5,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetServiceTar',
    full_name='gateway.Gateway.GetServiceTar',
    index=6,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetServiceEstimatedCost',
    full_name='gateway.Gateway.GetServiceEstimatedCost',
    index=7,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Payable',
    full_name='gateway.Gateway.Payable',
    index=8,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMetrics',
    full_name='gateway.Gateway.GetMetrics',
    index=9,
    containing_service=None,
    input_type=buffer__pb2._BUFFER,
    output_type=buffer__pb2._BUFFER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GATEWAY)

DESCRIPTOR.services_by_name['Gateway'] = _GATEWAY

# @@protoc_insertion_point(module_scope)

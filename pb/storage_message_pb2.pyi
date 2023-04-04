import memory_message_pb2 as _memory_message_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Storage(_message.Message):
    __slots__ = ["driver", "memory"]
    class Driver(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DRIVER_FIELD_NUMBER: _ClassVar[int]
    HDD: Storage.Driver
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    SSD: Storage.Driver
    UNKNOWN: Storage.Driver
    driver: Storage.Driver
    memory: _memory_message_pb2.Memory
    def __init__(self, driver: _Optional[_Union[Storage.Driver, str]] = ..., memory: _Optional[_Union[_memory_message_pb2.Memory, _Mapping]] = ...) -> None: ...

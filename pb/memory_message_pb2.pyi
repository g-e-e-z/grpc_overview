from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Memory(_message.Message):
    __slots__ = ["unit", "value"]
    class Unit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BIT: Memory.Unit
    BYTE: Memory.Unit
    GIGABYTE: Memory.Unit
    KILOBYTE: Memory.Unit
    MEGABYTE: Memory.Unit
    TERRABYTE: Memory.Unit
    UNIT_FIELD_NUMBER: _ClassVar[int]
    UNKOWN: Memory.Unit
    VALUE_FIELD_NUMBER: _ClassVar[int]
    unit: Memory.Unit
    value: int
    def __init__(self, value: _Optional[int] = ..., unit: _Optional[_Union[Memory.Unit, str]] = ...) -> None: ...

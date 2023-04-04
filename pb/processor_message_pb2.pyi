import memory_message_pb2 as _memory_message_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CPU(_message.Message):
    __slots__ = ["brand", "cores", "max_ghz", "min_ghz", "name", "number_threads"]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    CORES_FIELD_NUMBER: _ClassVar[int]
    MAX_GHZ_FIELD_NUMBER: _ClassVar[int]
    MIN_GHZ_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_THREADS_FIELD_NUMBER: _ClassVar[int]
    brand: str
    cores: int
    max_ghz: float
    min_ghz: float
    name: str
    number_threads: int
    def __init__(self, brand: _Optional[str] = ..., name: _Optional[str] = ..., cores: _Optional[int] = ..., number_threads: _Optional[int] = ..., min_ghz: _Optional[float] = ..., max_ghz: _Optional[float] = ...) -> None: ...

class GPU(_message.Message):
    __slots__ = ["brand", "max_ghz", "memory", "min_ghz", "name"]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    MAX_GHZ_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    MIN_GHZ_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    brand: str
    max_ghz: float
    memory: _memory_message_pb2.Memory
    min_ghz: float
    name: str
    def __init__(self, brand: _Optional[str] = ..., name: _Optional[str] = ..., min_ghz: _Optional[float] = ..., max_ghz: _Optional[float] = ..., memory: _Optional[_Union[_memory_message_pb2.Memory, _Mapping]] = ...) -> None: ...

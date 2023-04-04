import processor_message_pb2 as _processor_message_pb2
import memory_message_pb2 as _memory_message_pb2
import storage_message_pb2 as _storage_message_pb2
import screen_message_pb2 as _screen_message_pb2
import keyboard_message_pb2 as _keyboard_message_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Laptop(_message.Message):
    __slots__ = ["brand", "cpu", "gpus", "id", "keyboard", "name", "price_usd", "ram", "release_year", "screen", "storages", "updated_at", "weight_kg", "weight_lb"]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    GPUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KEYBOARD_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_USD_FIELD_NUMBER: _ClassVar[int]
    RAM_FIELD_NUMBER: _ClassVar[int]
    RELEASE_YEAR_FIELD_NUMBER: _ClassVar[int]
    SCREEN_FIELD_NUMBER: _ClassVar[int]
    STORAGES_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_KG_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_LB_FIELD_NUMBER: _ClassVar[int]
    brand: str
    cpu: _processor_message_pb2.CPU
    gpus: _containers.RepeatedCompositeFieldContainer[_processor_message_pb2.GPU]
    id: str
    keyboard: _keyboard_message_pb2.Keyboard
    name: str
    price_usd: float
    ram: _memory_message_pb2.Memory
    release_year: int
    screen: _screen_message_pb2.Screen
    storages: _containers.RepeatedCompositeFieldContainer[_storage_message_pb2.Storage]
    updated_at: _timestamp_pb2.Timestamp
    weight_kg: float
    weight_lb: float
    def __init__(self, id: _Optional[str] = ..., brand: _Optional[str] = ..., name: _Optional[str] = ..., cpu: _Optional[_Union[_processor_message_pb2.CPU, _Mapping]] = ..., ram: _Optional[_Union[_memory_message_pb2.Memory, _Mapping]] = ..., gpus: _Optional[_Iterable[_Union[_processor_message_pb2.GPU, _Mapping]]] = ..., storages: _Optional[_Iterable[_Union[_storage_message_pb2.Storage, _Mapping]]] = ..., screen: _Optional[_Union[_screen_message_pb2.Screen, _Mapping]] = ..., keyboard: _Optional[_Union[_keyboard_message_pb2.Keyboard, _Mapping]] = ..., weight_kg: _Optional[float] = ..., weight_lb: _Optional[float] = ..., price_usd: _Optional[float] = ..., release_year: _Optional[int] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

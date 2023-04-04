from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Screen(_message.Message):
    __slots__ = ["panel", "resolution", "size_inch", "touch"]
    class Panel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Resolution(_message.Message):
        __slots__ = ["height", "width"]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        height: int
        width: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    IPS: Screen.Panel
    PANEL_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    SIZE_INCH_FIELD_NUMBER: _ClassVar[int]
    TOUCH_FIELD_NUMBER: _ClassVar[int]
    UNKOWN: Screen.Panel
    VA: Screen.Panel
    panel: Screen.Panel
    resolution: Screen.Resolution
    size_inch: float
    touch: bool
    def __init__(self, size_inch: _Optional[float] = ..., resolution: _Optional[_Union[Screen.Resolution, _Mapping]] = ..., panel: _Optional[_Union[Screen.Panel, str]] = ..., touch: bool = ...) -> None: ...

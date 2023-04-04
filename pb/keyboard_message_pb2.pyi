from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Keyboard(_message.Message):
    __slots__ = ["backlit", "layout"]
    class Layout(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BACKLIT_FIELD_NUMBER: _ClassVar[int]
    DVORAK: Keyboard.Layout
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    QWERTY: Keyboard.Layout
    QWERTZ: Keyboard.Layout
    UNKOWN: Keyboard.Layout
    backlit: bool
    layout: Keyboard.Layout
    def __init__(self, layout: _Optional[_Union[Keyboard.Layout, str]] = ..., backlit: bool = ...) -> None: ...

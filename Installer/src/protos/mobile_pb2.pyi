"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class WireguardConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___WireguardConfigRequest = WireguardConfigRequest

@typing_extensions.final
class WireguardConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE64IMAGE_FIELD_NUMBER: builtins.int
    base64Image: builtins.str
    def __init__(
        self,
        *,
        base64Image: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base64Image", b"base64Image"]) -> None: ...

global___WireguardConfigResponse = WireguardConfigResponse
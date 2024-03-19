"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import grpc
import grpc.aio
import logs_pb2
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class LogsStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    StreamLogs: grpc.UnaryStreamMultiCallable[
        logs_pb2.LogRequest,
        logs_pb2.LogReply,
    ]
    GetLogs: grpc.UnaryStreamMultiCallable[
        logs_pb2.LogRequest,
        logs_pb2.LogReply,
    ]

class LogsAsyncStub:
    StreamLogs: grpc.aio.UnaryStreamMultiCallable[
        logs_pb2.LogRequest,
        logs_pb2.LogReply,
    ]
    GetLogs: grpc.aio.UnaryStreamMultiCallable[
        logs_pb2.LogRequest,
        logs_pb2.LogReply,
    ]

class LogsServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def StreamLogs(
        self,
        request: logs_pb2.LogRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[logs_pb2.LogReply], collections.abc.AsyncIterator[logs_pb2.LogReply]]: ...
    @abc.abstractmethod
    def GetLogs(
        self,
        request: logs_pb2.LogRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[logs_pb2.LogReply], collections.abc.AsyncIterator[logs_pb2.LogReply]]: ...

def add_LogsServicer_to_server(servicer: LogsServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

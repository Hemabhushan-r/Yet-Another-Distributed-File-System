# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dfs_pb2 as dfs__pb2


class DataTransferServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Message = channel.unary_unary(
                '/dfs.DataTransferService/Message',
                request_serializer=dfs__pb2.testM.SerializeToString,
                response_deserializer=dfs__pb2.testM.FromString,
                )
        self.UploadFile = channel.stream_unary(
                '/dfs.DataTransferService/UploadFile',
                request_serializer=dfs__pb2.FileData.SerializeToString,
                response_deserializer=dfs__pb2.Ack.FromString,
                )
        self.DownloadFile = channel.unary_stream(
                '/dfs.DataTransferService/DownloadFile',
                request_serializer=dfs__pb2.FileInfo.SerializeToString,
                response_deserializer=dfs__pb2.FileData.FromString,
                )
        self.FileSearch = channel.unary_unary(
                '/dfs.DataTransferService/FileSearch',
                request_serializer=dfs__pb2.FileInfo.SerializeToString,
                response_deserializer=dfs__pb2.Ack.FromString,
                )
        self.ReplicateFile = channel.stream_unary(
                '/dfs.DataTransferService/ReplicateFile',
                request_serializer=dfs__pb2.FileData.SerializeToString,
                response_deserializer=dfs__pb2.Ack.FromString,
                )
        self.FileList = channel.unary_unary(
                '/dfs.DataTransferService/FileList',
                request_serializer=dfs__pb2.UserInfo.SerializeToString,
                response_deserializer=dfs__pb2.UserFileList.FromString,
                )
        self.FileDelete = channel.unary_unary(
                '/dfs.DataTransferService/FileDelete',
                request_serializer=dfs__pb2.FileInfo.SerializeToString,
                response_deserializer=dfs__pb2.Ack.FromString,
                )
        self.UpdateFile = channel.stream_unary(
                '/dfs.DataTransferService/UpdateFile',
                request_serializer=dfs__pb2.FileData.SerializeToString,
                response_deserializer=dfs__pb2.Ack.FromString,
                )
        self.StoreFileChunk = channel.stream_unary(
                '/dfs.DataTransferService/StoreFileChunk',
                request_serializer=dfs__pb2.FileDataChunk.SerializeToString,
                response_deserializer=dfs__pb2.Ack.FromString,
                )
        self.GetFileChunk = channel.unary_stream(
                '/dfs.DataTransferService/GetFileChunk',
                request_serializer=dfs__pb2.FileDataChunkInfo.SerializeToString,
                response_deserializer=dfs__pb2.FileDataChunk.FromString,
                )
        self.IsDataNodeAlive = channel.unary_unary(
                '/dfs.DataTransferService/IsDataNodeAlive',
                request_serializer=dfs__pb2.Empty.SerializeToString,
                response_deserializer=dfs__pb2.DataNodeStats.FromString,
                )


class DataTransferServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Message(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FileSearch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicateFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FileList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FileDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StoreFileChunk(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFileChunk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsDataNodeAlive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataTransferServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Message': grpc.unary_unary_rpc_method_handler(
                    servicer.Message,
                    request_deserializer=dfs__pb2.testM.FromString,
                    response_serializer=dfs__pb2.testM.SerializeToString,
            ),
            'UploadFile': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=dfs__pb2.FileData.FromString,
                    response_serializer=dfs__pb2.Ack.SerializeToString,
            ),
            'DownloadFile': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=dfs__pb2.FileInfo.FromString,
                    response_serializer=dfs__pb2.FileData.SerializeToString,
            ),
            'FileSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.FileSearch,
                    request_deserializer=dfs__pb2.FileInfo.FromString,
                    response_serializer=dfs__pb2.Ack.SerializeToString,
            ),
            'ReplicateFile': grpc.stream_unary_rpc_method_handler(
                    servicer.ReplicateFile,
                    request_deserializer=dfs__pb2.FileData.FromString,
                    response_serializer=dfs__pb2.Ack.SerializeToString,
            ),
            'FileList': grpc.unary_unary_rpc_method_handler(
                    servicer.FileList,
                    request_deserializer=dfs__pb2.UserInfo.FromString,
                    response_serializer=dfs__pb2.UserFileList.SerializeToString,
            ),
            'FileDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.FileDelete,
                    request_deserializer=dfs__pb2.FileInfo.FromString,
                    response_serializer=dfs__pb2.Ack.SerializeToString,
            ),
            'UpdateFile': grpc.stream_unary_rpc_method_handler(
                    servicer.UpdateFile,
                    request_deserializer=dfs__pb2.FileData.FromString,
                    response_serializer=dfs__pb2.Ack.SerializeToString,
            ),
            'StoreFileChunk': grpc.stream_unary_rpc_method_handler(
                    servicer.StoreFileChunk,
                    request_deserializer=dfs__pb2.FileDataChunk.FromString,
                    response_serializer=dfs__pb2.Ack.SerializeToString,
            ),
            'GetFileChunk': grpc.unary_stream_rpc_method_handler(
                    servicer.GetFileChunk,
                    request_deserializer=dfs__pb2.FileDataChunkInfo.FromString,
                    response_serializer=dfs__pb2.FileDataChunk.SerializeToString,
            ),
            'IsDataNodeAlive': grpc.unary_unary_rpc_method_handler(
                    servicer.IsDataNodeAlive,
                    request_deserializer=dfs__pb2.Empty.FromString,
                    response_serializer=dfs__pb2.DataNodeStats.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dfs.DataTransferService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataTransferService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Message(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.DataTransferService/Message',
            dfs__pb2.testM.SerializeToString,
            dfs__pb2.testM.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/dfs.DataTransferService/UploadFile',
            dfs__pb2.FileData.SerializeToString,
            dfs__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dfs.DataTransferService/DownloadFile',
            dfs__pb2.FileInfo.SerializeToString,
            dfs__pb2.FileData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FileSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.DataTransferService/FileSearch',
            dfs__pb2.FileInfo.SerializeToString,
            dfs__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicateFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/dfs.DataTransferService/ReplicateFile',
            dfs__pb2.FileData.SerializeToString,
            dfs__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FileList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.DataTransferService/FileList',
            dfs__pb2.UserInfo.SerializeToString,
            dfs__pb2.UserFileList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FileDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.DataTransferService/FileDelete',
            dfs__pb2.FileInfo.SerializeToString,
            dfs__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/dfs.DataTransferService/UpdateFile',
            dfs__pb2.FileData.SerializeToString,
            dfs__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StoreFileChunk(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/dfs.DataTransferService/StoreFileChunk',
            dfs__pb2.FileDataChunk.SerializeToString,
            dfs__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFileChunk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dfs.DataTransferService/GetFileChunk',
            dfs__pb2.FileDataChunkInfo.SerializeToString,
            dfs__pb2.FileDataChunk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IsDataNodeAlive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.DataTransferService/IsDataNodeAlive',
            dfs__pb2.Empty.SerializeToString,
            dfs__pb2.DataNodeStats.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import train_pb2 as train__pb2


class TrainServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LoadDataSet = channel.unary_unary(
                '/pca.TrainService/LoadDataSet',
                request_serializer=train__pb2.DataPrepareRequest.SerializeToString,
                response_deserializer=train__pb2.DataPrepareResponse.FromString,
                )
        self.Train = channel.unary_stream(
                '/pca.TrainService/Train',
                request_serializer=train__pb2.TrainRequest.SerializeToString,
                response_deserializer=train__pb2.TrainResponse.FromString,
                )
        self.Test = channel.unary_unary(
                '/pca.TrainService/Test',
                request_serializer=train__pb2.TestRequest.SerializeToString,
                response_deserializer=train__pb2.TestResponse.FromString,
                )


class TrainServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def LoadDataSet(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Train(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Test(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrainServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LoadDataSet': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadDataSet,
                    request_deserializer=train__pb2.DataPrepareRequest.FromString,
                    response_serializer=train__pb2.DataPrepareResponse.SerializeToString,
            ),
            'Train': grpc.unary_stream_rpc_method_handler(
                    servicer.Train,
                    request_deserializer=train__pb2.TrainRequest.FromString,
                    response_serializer=train__pb2.TrainResponse.SerializeToString,
            ),
            'Test': grpc.unary_unary_rpc_method_handler(
                    servicer.Test,
                    request_deserializer=train__pb2.TestRequest.FromString,
                    response_serializer=train__pb2.TestResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pca.TrainService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TrainService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def LoadDataSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pca.TrainService/LoadDataSet',
            train__pb2.DataPrepareRequest.SerializeToString,
            train__pb2.DataPrepareResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Train(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pca.TrainService/Train',
            train__pb2.TrainRequest.SerializeToString,
            train__pb2.TrainResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Test(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pca.TrainService/Test',
            train__pb2.TestRequest.SerializeToString,
            train__pb2.TestResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

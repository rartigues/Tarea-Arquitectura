# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api_proto import villain_pb2 as api__proto_dot_villain__pb2


class VillainServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddVillain = channel.unary_unary(
                '/VillainService/AddVillain',
                request_serializer=api__proto_dot_villain__pb2.VillainRequest.SerializeToString,
                response_deserializer=api__proto_dot_villain__pb2.VillainResponse.FromString,
                )


class VillainServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddVillain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VillainServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddVillain': grpc.unary_unary_rpc_method_handler(
                    servicer.AddVillain,
                    request_deserializer=api__proto_dot_villain__pb2.VillainRequest.FromString,
                    response_serializer=api__proto_dot_villain__pb2.VillainResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'VillainService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VillainService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddVillain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VillainService/AddVillain',
            api__proto_dot_villain__pb2.VillainRequest.SerializeToString,
            api__proto_dot_villain__pb2.VillainResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

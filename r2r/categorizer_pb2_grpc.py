# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import categorizer_pb2 as categorizer__pb2


class CategorizerStub(object):
    """The categprozation service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Categorize = channel.unary_unary(
                '/categorizer.Categorizer/Categorize',
                request_serializer=categorizer__pb2.CategorizationRequest.SerializeToString,
                response_deserializer=categorizer__pb2.CategorizationResponse.FromString,
                )


class CategorizerServicer(object):
    """The categprozation service definition.
    """

    def Categorize(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CategorizerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Categorize': grpc.unary_unary_rpc_method_handler(
                    servicer.Categorize,
                    request_deserializer=categorizer__pb2.CategorizationRequest.FromString,
                    response_serializer=categorizer__pb2.CategorizationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'categorizer.Categorizer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Categorizer(object):
    """The categprozation service definition.
    """

    @staticmethod
    def Categorize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/categorizer.Categorizer/Categorize',
            categorizer__pb2.CategorizationRequest.SerializeToString,
            categorizer__pb2.CategorizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

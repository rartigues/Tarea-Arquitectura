import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from api.models import Villain
from gRPCClient.serializers import VillainProtoSerializer


class VillainService(Service):
    def Create(self, request, context):
        serializer = VillainProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message


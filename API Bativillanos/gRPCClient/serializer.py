from django_grpc_framework import proto_serializers
from api.models import Villain
from api_proto import client_pb2


class PostProtoSerializer(proto_serializers.ModelProtoSerializer):  
    class Meta:
        model = Villain
        proto_class = client_pb2.Villain
        fields = ['usuario', 'fecha_ingreso']

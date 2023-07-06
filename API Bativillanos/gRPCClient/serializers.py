from django_grpc_framework import proto_serializers
from api.models import Villain
from api_proto import villain_pb2


class VillainProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Villain
        proto_class = villain_pb2.Post
        fields = ['nombre_villano', 'fecha_ingreso']
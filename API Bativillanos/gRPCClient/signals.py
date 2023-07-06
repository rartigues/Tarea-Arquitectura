from api.models import Villain
from django.db.models.signals import post_save
from django.dispatch import receiver
import grpc
from api_proto import villain_pb2
from api_proto import villain_pb2_grpc
import datetime
from google.protobuf.timestamp_pb2 import Timestamp

@receiver(post_save, sender=Villain, dispatch_uid='enviar_protobuf')
def enviar_protobuf(sender, instance, created, **kwargs):
    if created:

        channel = grpc.insecure_channel('localhost:50051')
        client = villain_pb2_grpc.VillainServiceStub(channel)

        now = datetime.datetime.now()
        timestamp = Timestamp()
        timestamp.FromDatetime(now)
    
        response = client.AddVillain(
            villain_pb2.VillainRequest(
                nombre_villano=instance.nombre, 
                fecha_ingreso=timestamp,
            )
        )
from rest_framework.views import APIView
from .serializer import VillainSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Villain

# Create your views here.

class VillainView(APIView):
    def post(self, request):
        serializer = VillainSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        
        serializer.save()

        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    
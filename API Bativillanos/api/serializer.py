from rest_framework import serializers
from .models import Villain, Power

class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Power
        fields = [
            'nombre',
        ]

class VillainSerializer(serializers.ModelSerializer):
    poderes = PowerSerializer(
        many=True
    )

    class Meta:
        model  = Villain
        fields = [
            'nombre',
            'universo',
            'poderes',
            'descripcion',
            'imagen',
        ]
    
    def create(self, validated_data):
        powers_data = validated_data.pop('poderes')

        villain = Villain.objects.create(
            **validated_data,
        )

        for power in powers_data:
            Power.objects.create(
                villano=villain,
                **power,
            )

        return villain
        
        


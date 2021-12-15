from rest_framework import serializers
from .models import Mascotas

class MascotaSerializable(serializers.ModelSerializer):
    class meta:
        model=Mascotas
        fields=(
            'nombre',
            'tipo_mascota',
            'raza',
            'edad'
        )

class AccesorioSerializable(serializers.ModelSerializer):
    class meta:
        model=Mascotas
        fields=(
            'nombre',
            'cantidad',
            'valor'
        )

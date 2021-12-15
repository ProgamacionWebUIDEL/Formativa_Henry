from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MascotaSerializable
from .serializers import AccesorioSerializable
from .serializers import AlimentoSerializable

from .models import Accesorios, Mascotas

# Create your views here.
class MascotaVista(viewsets.ModelViewsets):
    serializer_class:MascotaSerializable
    queryset=Mascotas.objects.all()
class AccesorioVista(viewsets.ModelViewsets):
    serializer_class:AccesorioSerializable
    queryset=Accesorios.objects.all()
class AlimentosVista(viewsets.ModelViewsets):
    serializer_class:AlimentoSerializable
    queryset=Accesorios.objects.all()
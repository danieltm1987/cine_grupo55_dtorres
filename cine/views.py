from rest_framework import viewsets
from cine.serializers import *
from cine.models import *


class Cine_view(viewsets.ModelViewSet):
    queryset = Cine.objects.all()
    serializers_class = Cine_serializer


class Sala_view(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializers_class = Sala_serializer


class Pelicula_view(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializers_class = Pelicula_serializer


class Funcion_view(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()
    serializers_class = Funcion_serializer


class Boleta_view(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializers_class = Boleta_serializer


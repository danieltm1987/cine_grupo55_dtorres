from rest_framework import viewsets
from cine.serializers import *
from cine.models import *


class Cine_view(viewsets.ModelViewSet):
    queryset = Cine.objects.all()
    serializer_class = Cine_serializer


class Sala_view(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = Sala_serializer


class Pelicula_view(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = Pelicula_serializer


class Funcion_view(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()
    serializer_class = Funcion_serializer


class Boleta_view(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = Boleta_serializer


class Cliente_view(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = Cliente_serializer



class Prueba_view(viewsets.ModelViewSet):
    def get_queryset(self):
        dato = self.request.query_params.get('dato')


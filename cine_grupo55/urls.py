from django.urls import path, include
from rest_framework import routers
from cine.views import *

router = routers.DefaultRouter()
router.register('cine',Cine_view,basename='cine')
router.register('sala',Sala_view,basename='sala')
router.register('pelicula',Pelicula_view,basename='pelicula')
router.register('funcion',Funcion_view,basename='funcion')
router.register('cliente',Cliente_view,basename='cliente')
router.register('boleta',Boleta_view,basename='boleta')


urlpatterns = [
    path('',include(router.urls))
]

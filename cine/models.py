from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Cine(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre




class Sala(models.Model):
    cine = models.ForeignKey(Cine, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    numero_asientos = models.IntegerField()

    def __str__(self):
        return self.cine.nombre + ' - ' + self.nombre


class Pelicula(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.CharField(max_length=5)
    genero = models.CharField(max_length=20)
    director = models.CharField(max_length=20)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre + ' - ' + self.genero


class Usuario(AbstractUser):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    token = models.CharField(max_length=100)



class Funcion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    fecha = models.DateField(auto_now_add=True)
    valor = models.IntegerField()
    hora = models.DateTimeField()

    def __str__(self):
        return self.pelicula.nombre + ' - ' + self.sala.nombre + ' - ' + str(self.sala.numero_asientos) + ' asientos  - ' + str(self.valor)


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ' - ' + self.correo


class Boleta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    funcion = models.ForeignKey(Funcion, on_delete=models.PROTECT)
    asientos = models.IntegerField()
    valor_boleta = models.IntegerField()


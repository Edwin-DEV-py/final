from distutils.command.upload import upload
from django.db import models
import random,string
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth.models import AbstractUser,BaseUserManager
from pytz import timezone

class Perfil(models.Model):
    nombre = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Perfil de {self.nombre.username}'


    
class Auto(models.Model):
    placa = models.CharField(max_length=6)
    modelo = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    foto_v = models.ImageField(upload_to='vehiculos',null=True)
    foto_tarjeta = models.ImageField(upload_to='propiedad',null=True)
    aprobado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.placa


lista_direcciones = [
    ('Calle','Cl'),
    ('Carrera','Cra'),
    ('Diagonal','Dg'),
    ('Transversal','Tr'),
    ('Avenida','Av'),
]

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    direccion_inicio = models.CharField(
        max_length=11,
        choices=lista_direcciones,
        default="Cl"
    )
    cc_ini = models.CharField(max_length=10)
    numero_ini = models.CharField(max_length=10)
    extra_ini = models.CharField(max_length=100)
    direccion_fin = models.CharField(
        max_length=11,
        choices=lista_direcciones,
        default="Cl"
    )
    cc_fin = models.CharField(max_length=10)
    numero_fin = models.CharField(max_length=10)
    extra_fin = models.CharField(max_length=100)
    
    
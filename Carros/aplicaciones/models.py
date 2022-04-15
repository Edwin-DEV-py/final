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

class auto(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    placa = models.CharField(max_length=6)
    modelo = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    foto_v = models.ImageField(upload_to='vehiculos',null=True)
    foto_tarjeta = models.ImageField(upload_to='propiedad',null=True)
        
    def __str__(self):
        return f'{self.user.username}: {self.placa},{self.foto_v},{self.foto_v},{self.foto_tarjeta}'
    
    
class automovil(models.Model):
    foto_v = models.ImageField(upload_to="vehiculos_fotos")
    
    class Meta:
        verbose_name = 'automovil'
        
    def __str__(self):
        return f'Foto: {self.foto_v}'
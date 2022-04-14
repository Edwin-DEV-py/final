from distutils.command.upload import upload
from django.db import models


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    username = models.CharField('nombre',max_length=50)
    apellido = models.CharField('apellido',max_length=50,null=True)
    telefono = models.CharField('telefono',max_length=10,null=True)
    cedula = models.CharField('cedula',max_length=10,null=True)
    direccion = models.CharField('direccion',max_length=150,null=True)
    foto = models.ImageField(upload_to='Fotografias',null=True)
    certificado = models.ImageField(upload_to='certificados',null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','cedula']
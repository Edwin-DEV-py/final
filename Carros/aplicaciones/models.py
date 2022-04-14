from distutils.command.upload import upload
from django.db import models
import random,string
from django.utils.text import slugify
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser,BaseUserManager

class Perfil(models.Model):
    nombre = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Perfil de {self.nombre.username}'
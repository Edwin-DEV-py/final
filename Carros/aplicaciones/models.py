from distutils.command.upload import upload
from django.db import models
import random,string
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth.models import AbstractUser,BaseUserManager
from pytz import timezone

from django.db.models.signals import post_save

class Perfil(models.Model):
    nombre = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars',blank=True)

    def __str__(self):
        return f'Perfil de {self.nombre.username}'
    
def create_profile(sender, instance, created, *kwargs):
    if created:
        Perfil.objects.create(user=instance)
        

    
        


    
class Autos(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='autos')
    placa = models.CharField(max_length=6)
    modelo = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    foto_v = models.ImageField(upload_to='vehiculos',null=True)
    foto_tarjeta = models.ImageField(upload_to='propiedad',null=True)
    aprobado = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username}:{self.placa},{self.aprobado}'
    
class post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    contenido = models.TextField(max_length=100)
    
    def __str__(self):
        return f'{self.user.username}:{self.contenido}'


lista_direcciones = [
    ('Calle','Cl'),
    ('Carrera','Cra'),
    ('Diagonal','Dg'),
    ('Transversal','Tr'),
    ('Avenida','Av'),
]

class Direccion(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='direcciones')
    id = models.AutoField(primary_key=True)
    direccion_inicio = models.CharField(
        max_length=11,
        choices=lista_direcciones,
        default="Cl"
    )
    cc_ini = models.CharField(max_length=10)
    numero_ini = models.CharField(max_length=10)
    extra_ini = models.CharField(max_length=100)
    direccion_2 = models.CharField(
        max_length=11,
        choices=lista_direcciones,
        default="Cl",
        blank=True,
    )
    cc_2 = models.CharField(max_length=10,blank=True)
    numero_2 = models.CharField(max_length=10,blank=True)
    extra_2 = models.CharField(max_length=100,blank=True)
    direccion_3 = models.CharField(
        max_length=11,
        choices=lista_direcciones,
        default="Cl",
        blank=True
    )
    cc_3 = models.CharField(max_length=10,blank=True)
    numero_3 = models.CharField(max_length=10,blank=True)
    extra_3 = models.CharField(max_length=100,blank=True)
    direccion_4 = models.CharField(
        max_length=11,
        choices=lista_direcciones,
        default="Cl",
        blank=True
    )
    cc_4 = models.CharField(max_length=10,blank=True)
    numero_4 = models.CharField(max_length=10,blank=True)
    extra_4 = models.CharField(max_length=100,blank=True)
    direccion_fin = models.CharField(
        max_length=11,
        choices=lista_direcciones,
        default="Cl",
        blank=True
    )
    cc_fin = models.CharField(max_length=10)
    numero_fin = models.CharField(max_length=10)
    extra_fin = models.CharField(max_length=100)
    
    fecha = models.DateTimeField(verbose_name='Fecha',blank=True,null=True)
    
    liked = models.ManyToManyField(User,blank=True, related_name='liked')
    
    


    
    
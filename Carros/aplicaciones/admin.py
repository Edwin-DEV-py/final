from django.contrib import admin
from .models import User, Autos,Perfil,Direccion

admin.register(User)
admin.site.register(Autos)
admin.site.register(Perfil)
admin.site.register(Direccion)


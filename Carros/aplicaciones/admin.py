from django.contrib import admin
from .models import User, Autos,Perfil

admin.register(User)
admin.site.register(Autos)
admin.site.register(Perfil)

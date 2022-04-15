from django.contrib import admin
from .models import User, auto

admin.register(User)
admin.site.register(auto)

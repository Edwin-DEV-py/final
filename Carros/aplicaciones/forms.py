from dataclasses import field
from email.policy import default
import re
from django import forms
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *

class Formulario_registro_usuario(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    username = forms.EmailField(label="Email",widget=forms.EmailInput)
    last_name = forms.CharField(label="Apellido")
    telefono = forms.CharField(label="Telefono")
    cedula = forms.CharField(label="cedula")
    direccion = forms.CharField(label="Direccion")
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2','telefono','cedula']
        help_texts = {k:"" for k in fields}
        
        

        
class CustomerForm(ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'
        exclude = ['user','aprobado']
        
class Direcciones(ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__'
        exclude = ['user']
        
        

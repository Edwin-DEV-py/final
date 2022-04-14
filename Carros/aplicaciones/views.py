from ast import For
from this import d
from django.shortcuts import render,redirect
from .models import *
from .forms import Formulario_registro_usuario
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http.response import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request,'index.html')

def iniciar_seccion(request):
    return render(request,'iniciar_sesion.html')

def registrarse(request):
    if request.method == 'POST':
        form = Formulario_registro_usuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
            return redirect('index.html')
    else:
        form = Formulario_registro_usuario()
    contexto = {'form':form}
    return render(request,'registrarse.html',contexto)
        

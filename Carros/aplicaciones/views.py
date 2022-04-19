from ast import For
from this import d
from time import time
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CustomerForm, Formulario_registro_usuario
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http.response import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request,'index.html')

def iniciar_seccion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            is_active = form.cleaned_data.get("is_active")
            usuario = authenticate(username=username,password = password,is_active=True)
            if usuario is not None:
                login(request,usuario)
                messages.success(request,f'bienvenido {username}')
                return redirect('index.html')
            else:
                messages.error(request,"Los datos son incorrectos")
    form = AuthenticationForm()
    return render(request,'iniciar_sesion.html',{"form":form})

def salir(request):
    logout(request)
    return redirect("index")

def perfil(request):
    return render(request,'perfil.html')

def post2(request):
    usuario = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        formulario = CustomerForm(request.POST, request.FILES)
        if formulario.is_valid():
            post = formulario.save(commit = False)
            post.user = usuario
            post.save()
            return redirect('index.html')
    else:
        formulario = CustomerForm()
    return render(request,'post2.html',{'form':formulario})

def registrarse(request):
    if request.method == 'POST':
        form = Formulario_registro_usuario(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active=False
            user.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
            return redirect('index.html')
    else:
        form = Formulario_registro_usuario()
    contexto = {'form':form}
    return render(request,'registrarse.html',contexto)

def rutasconductor(request):
    return render(request,"rutas_conductor.html")
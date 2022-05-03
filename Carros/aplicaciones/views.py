from ast import For
import imp
from this import d
from time import time
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CustomerForm, Formulario_registro_usuario,Direcciones, postform
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http.response import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

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
    usuario = Autos.objects.filter(user_id = request.user.id)
    rutas = Direccion.objects.filter(user_id = request.user.id)
    return render(request,'perfil.html',{'u':usuario,'r':rutas})

@login_required
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


@login_required
def rutasconductor(request):
    usuario = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        formulario = Direcciones(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit = False)
            post.user = usuario
            post.save()
            return redirect('index.html')
        else:
            messages.success(request,'vehiculo no aprobado') 
            return redirect('perfil.html')
    else:
        formulario = Direcciones()
    contexto = {'form':formulario}
    return render(request,"rutas_conductor.html",contexto)

def rutas(request):
    rutas = Direccion.objects.all()
    user = request.user
    contexto = {
        'user': user,
        'rutas':rutas
    }
    return render(request,"home_rutas.html",contexto)

def editarrutas(request,id):
    rutas = Direccion.objects.get(id=id)
    if request.method == 'GET':
        form = Direcciones(instance=rutas)
        contesto = {'form':form}
    else:
        form = Direcciones(request.POST, instance=rutas)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'rutas_conductor.html',contesto)

def terminarruta(request,id):
    rutas = Direccion.objects.get(id=id)
    rutas.delete()
    return redirect('index')



def darlike(request,pk):
    post = Direccion.objects.get(pk=pk)
    like = False
    for like in post.liked.filter(id=request.user.id):
        if like == request.user:
            like = True
            break
    if not like:
        post.liked.add(request.user)
    if like:
        post.liked.remove(request.user)
                
    next = request.POST.get('next','/')
    return HttpResponseRedirect(next)

def perfiles(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username = username)
        post = user.direcciones.all()
    else:
        post = current_user.direcciones.all()
        user = current_user
    contexto = {
        'user':user,
        'post':post,
    }
    return render(request, 'perfil.html',contexto)

            

from django import forms
from django.shortcuts import redirect, render
from .backend import MyBackend
from .forms import ComentarioForm, JuegosForm, LoginForm, UsuarioForms, VoluntariosForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Comentario, Juegos, Usuarios

# Create your views here.

myBackend = MyBackend()

def index(request, backend='supergame.backend.MyBackend'):
    if request.method== 'POST':
        form = LoginForm(data= request.POST)
        if form.is_valid():
            usuario=form.cleaned_data["email"]
            clave=form.cleaned_data["contrasena"]
            user=myBackend.authenticate(request,username=usuario, password=clave)
            if user is not None:
                login(request,user, backend='supergame.backend.MyBackend')
                return redirect(juegos)
            else:
                return render(request, 'supergame/noexiste.html')
    else:
        form = LoginForm()
        return render(request, 'supergame/index.html',{'form':form})


@login_required(login_url="/")
def salir(request):
    logout(request)
    return redirect(index)


def registrate(request):    
    if request.method == 'POST':
        form = UsuarioForms(data= request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
        return redirect(index)
    else:
        form= UsuarioForms()
        return render(request, 'supergame/registrate.html',{'form':form})


@login_required(login_url="/")
def quienessomos(request):
    return render(request, 'supergame/quienessomos.html')


@login_required(login_url="/")
def usuariosCreados(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'supergame/usuariosCreados.html',{'usuarios':usuarios})


@login_required(login_url="/")
def comentarios(request):
    if request.method== "POST":
        form= ComentarioForm(data= request.POST)
        comentario= form.save(commit= False)
        comentario.save()
        return redirect(comentariosList)
    else:
        form = ComentarioForm()
        return render(request, "supergame/comentarioUsuarios.html",{"form":form})


@login_required(login_url="/")  
def comentariosList(request):
    comentarios= Comentario.objects.all()
    return render(request, 'supergame/comentariosList.html',{"comentarios":comentarios})


def editar_comentario(request, id):
    comentario = Comentario.objects.get(pk=id)
    if request.method== 'POST':
        form= ComentarioForm(data=request.POST, instance= comentario)
        form.save()
        return redirect(comentariosList)
    else:
        form= ComentarioForm(instance= comentario)
        return render(request, 'supergame/editar_comentario.html', {"form":form})


def eliminar_comentario(request, id):
    comentario= Comentario.objects.get(pk=id)
    comentario.delete()
    return redirect(comentariosList)


@login_required(login_url="/")
def voluntarios(request):
    if request.method== 'POST':
        form = VoluntariosForm(data = request.POST)
        if form.is_valid:
            voluntarioss= form.save(commit=False)
            voluntarioss.save()
            return render(request,'supergame/Voluntariocreado.html')
    else:
        form= VoluntariosForm()
        return render(request, 'supergame/crearVoluntarios.html',{'form':form})


@login_required(login_url="/")
def juegos(request):
    juegoss = Juegos.objects.all()
    return render(request, 'supergame/juegos.html',{'juegos':juegoss})


def editar_juegos(request, id):
    juegoss = Juegos.objects.get(pk=id)
    if request.method== 'POST':
        form= JuegosForm(data=request.POST, instance= juegoss)
        form.save()
        return redirect(juegos)
    else:
        form= JuegosForm(instance= juegoss)
        return render(request, 'supergame/editar_juegos.html', {"form":form})


def eliminar_juegos(request, id):
    juegoss= Juegos.objects.get(pk=id)
    juegoss.delete()
    return redirect(juegos)


@login_required(login_url="/")
def publicar(request):
    if request.method=='POST':
        form= JuegosForm(data= request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
        return redirect(juegos)
    else:
        form= JuegosForm()
        return render(request, 'supergame/publicar.html',{'form':form})
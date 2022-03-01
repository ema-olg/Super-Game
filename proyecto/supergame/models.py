from django import forms
from django.db import models
from django.db.models.deletion import SET_NULL
from django.forms import widgets


class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.CharField(max_length=50)
    sexo= models.CharField(max_length=50)
    email= models.CharField(max_length=50, unique=True)
    contrasena= models.CharField(max_length=50)
    last_login= models.CharField(max_length=50, null=True)
    is_authenticated = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    nombre=models.CharField(max_length=40, default='nombre')
    email=models.CharField(max_length=50)
    comentario=models.CharField(max_length=140)

    def __str__(self):
        return self.email

    
class NivelRes(models.Model):
    nivel= models.CharField(max_length=7, primary_key= True)

    def __str__(self):
        return self.nivel


class Voluntarios(models.Model):
    nombre= models.CharField(max_length= 50)
    email= models.CharField(max_length=50)
    telefono= models.IntegerField()
    nivel= models.ForeignKey(NivelRes, null=True, on_delete=models.SET_NULL)


class Juegos(models.Model):
    titulo = models.CharField(max_length=13)
    imagen= models.ImageField(upload_to= 'juegos', null= True)
    descripcion= models.CharField(max_length=140)
    presio= models.IntegerField()

class Jugadores(models.Model):
    nombres= models.CharField(max_length=40)

class Ganadores(models.Model):
    nombres= models.CharField(max_length=40)
from django import forms
from django.db import models
from django.db.models import fields
from django.forms.widgets import Widget
from .models import Comentario, Juegos, Usuarios, Voluntarios


class UsuarioForms(forms.ModelForm):
    class Meta:
        model= Usuarios
        fields = ('nombre', 'apellido', 'edad','sexo', 'email', 'contrasena')

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    contrasena = forms.CharField(widget=forms.PasswordInput)


class ComentarioForm(forms.ModelForm):
    class Meta:
        model= Comentario
        fields= ('nombre', 'email', 'comentario')

class VoluntariosForm(forms.ModelForm):
    class Meta:
        model= Voluntarios
        fields= ('nombre', 'email', 'telefono', 'nivel')

class JuegosForm(forms.ModelForm):
    class Meta:
        model= Juegos
        fields= ('titulo', 'imagen', 'descripcion', 'presio')
    
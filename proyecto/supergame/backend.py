from django.contrib.auth.backends import BaseBackend
from .models import Usuarios

class MyBackend(BaseBackend):
    def authenticate(self, request, username= None, password= None):
        try:
            usuario= Usuarios.objects.filter(email= username, contrasena= password).get()
            return usuario
        except:
            return None
    
    def get_user(self, user_id):
        try:
            return Usuarios.objects.get(pk = user_id)
        except Usuarios.DoesNotExist:
            return None
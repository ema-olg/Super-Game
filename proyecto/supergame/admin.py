from django.contrib import admin

from .models import Comentario, Juegos, NivelRes, Usuarios, Voluntarios

# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Comentario)
admin.site.register(NivelRes)
admin.site.register(Voluntarios)
admin.site.register(Juegos)

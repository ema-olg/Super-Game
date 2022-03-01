from django.urls import path
from supergame import views

urlpatterns =[
    path('', views.index),
    path('registrate', views.registrate),
    path('quienessomos', views.quienessomos),
    path('salir', views.salir),
    path('usuariosCreados', views.usuariosCreados),
    path('comentarios', views.comentarios),
    path('comentariosList', views.comentariosList),
    path('editarr/<int:id>/',views.editar_comentario),
    path('eliminarr/<int:id>/', views.eliminar_comentario),
    path('juegos', views.juegos),
    path('editar/<int:id>/', views.editar_juegos),
    path('eliminar/<int:id>/', views.eliminar_juegos),
    path('publicar', views.publicar)
]
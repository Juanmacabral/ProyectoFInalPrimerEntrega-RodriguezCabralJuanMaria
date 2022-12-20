from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),

    path('biblioteca/', biblioteca, name="biblioteca"),
    path('agregarlibro/', agregarlibro, name="agregarlibro"),
    path('buscadorlibro/', buscadorlibro, name="buscadorlibro"),
    path('buscarlibro/', buscarlibro, name="buscarlibro"),

    path('videoteca/', videoteca, name="videoteca"),
    path('agregarpelicula/', agregarpelicula, name="agregarpelicula"),
    path('buscadorpelicula/', buscadorpelicula, name="buscadorpelicula"),
    path('buscarpelicula/', buscarpelicula, name="buscarpelicula"),

    path('discoteca/', discoteca, name="discoteca"),
    path('agregardisco/', agregardisco, name="agregardisco"),
    path('buscadordisco/', buscadordisco, name="buscadordisco"),
    path('buscardisco/', buscardisco, name="buscardisco"),
                ]

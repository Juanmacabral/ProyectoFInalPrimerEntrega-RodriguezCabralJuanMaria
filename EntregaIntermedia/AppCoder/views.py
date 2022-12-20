from django.shortcuts import render
from .models import Biblioteca, Videoteca, Discoteca
from .forms import BibliotecaForm, VideotecaForm, DiscotecaForm


# Create your views here.
def inicio(request):
    return render(request, "AppCoder/inicio.html")

def biblioteca(request):
    return render(request, "AppCoder/biblioteca.html")


def agregarlibro(request):
    if request.method == "POST":
        form = BibliotecaForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data  # convierte el formulario en un diccionario para poder manejarlo y guardarlo en la DB.
            print(informacion)
            autor = informacion["autor"]
            libro = informacion["libro"]
            genero = informacion["genero"]
            paginas = informacion["paginas"]
            libros = Biblioteca(autor=autor, libro=libro, genero=genero, paginas=paginas)
            libros.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "libro guardado"})
        else:
            return render(request, "AppCoder/agregarlibro.html", {"mensaje2": "Informacion no Valida para guardar."})
    else:
        formulario = BibliotecaForm()
        return render(request, "AppCoder/agregarlibro.html", {"form": formulario})

def buscadorlibro(request):
    return render(request, "AppCoder/buscadorlibro.html")

def buscarlibro(request):
    libro= request.GET["libro"]
    if libro!="":
        libros= Biblioteca.objects.filter(libro=libro)
        return render(request, "AppCoder/busquedalibro.html", {"libros":libros})
    else:
        return render(request, "AppNueva/buscadorlibro.html", {"mensaje" : "el libro solicitada no se encuentra en la base de datos"})

def videoteca(request):
    return render(request, "AppCoder/videoteca.html")


def agregarpelicula(request):
    if request.method == "POST":
        form = VideotecaForm(request.POST)

        if form.is_valid():
            informacion2 = form.cleaned_data  # convierte el formulario en un diccionario para poder manejarlo y guardarlo en la DB.
            print(informacion2)
            titulo = informacion2["titulo"]
            director = informacion2["directos"]
            fecha_estreno = informacion2["fecha_estreno"]
            pelis = Videoteca(titulo=titulo, director=director, fecha_estreno=fecha_estreno)
            pelis.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "pelicula guardada"})
        else:
            return render(request, "AppCoder/agregarpelicula.html", {"mensaje2": "Informacion no Valida para guardar."})
    else:
        formulario = VideotecaForm()
        return render(request, "AppCoder/agregarpelicula.html", {"form": formulario})

def buscadorpelicula(request):
    return render(request, "AppCoder/buscadorpelicula.html")

def buscarpelicula(request):
    titulo= request.GET["titulo"]
    if titulo!="":
        pelis= Videoteca.objects.filter(titulo=titulo)
        return render(request, "AppCoder/busquedapelicula.html", {"pelis":pelis})
    else:
        return render(request, "AppNueva/buscadorpelicula.html", {"mensaje" : "la pelicula solicitada no se encuentra en la base de datos"})

def discoteca(request):
    return render(request, "AppCoder/discoteca.html")


def agregardisco(request):
    if request.method == "POST":
        form = DiscotecaForm(request.POST)

        if form.is_valid():
            informacion3 = form.cleaned_data  # convierte el formulario en un diccionario para poder manejarlo y guardarlo en la DB.
            print(informacion3)
            artista = informacion3["artista"]
            disco = informacion3["disco"]
            cantidad_canciones = informacion3["cantidad_canciones"]
            discos = Discoteca(artista=artista, disco=disco, cantidad_canciones=cantidad_canciones)
            discos.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "disco guardado"})
        else:
            return render(request, "AppCoder/agregardisco.html", {"mensaje2": "Informacion no Valida para guardar."})
    else:
        formulario = DiscotecaForm()
        return render(request, "AppCoder/agregardisco.html", {"form": formulario})

def buscadordisco(request):
    return render(request, "AppCoder/buscadordisco.html")

def buscardisco(request):
    disco= request.GET["disco"]
    if disco!="":
        discos= Discoteca.objects.filter(disco=disco)
        return render(request, "AppCoder/busquedadisco.html", {"discos":discos})
    else:
        return render(request, "AppNueva/buscadordisco.html", {"mensaje" : "el disco solicitado no se encuentra en la base de datos"})



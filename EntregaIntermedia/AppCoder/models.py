from django.db import models


class Biblioteca(models.Model):
    autor = models.CharField(max_length=50)
    libro = models.CharField (max_length=50)
    genero = models.CharField (max_length=50)
    paginas= models.IntegerField()

    def __str__(self):
        return f"{(self.autor)} + {(self.libro)} + {(self.genero)} + {str(self.paginas)}"

class Videoteca(models.Model):
    titulo = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    fecha_estreno = models.DateField(auto_created=False, auto_now=False, blank=True)

    def __str__(self):
        return f"{(self.titulo)} + {(self.director)} + {(self.fecha_estreno)}"


class Discoteca(models.Model):
    artista = models.CharField(max_length=50)
    disco = models.CharField(max_length=50)
    cantidad_canciones = models.IntegerField()

    def __str__(self):
        return f"{(self.artista)} + {(self.disco)} + {(self.cantidad_canciones)}"
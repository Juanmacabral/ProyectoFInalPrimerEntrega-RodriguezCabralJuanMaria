from django import forms

class BibliotecaForm (forms.Form):
    autor = forms.CharField (label="autor", max_length=50)
    libro = forms.CharField (label="libro", max_length=50)
    genero = forms.CharField (label="genero", max_length=50)
    paginas = forms.IntegerField(label="paginas")

class VideotecaForm(forms.Form):
    titulo = forms.CharField(label="pelicula", max_length=50)
    director = forms.CharField(label="director", max_length=50)
    fecha_estreno = forms.DateField(label="fecha_estreno")

class DiscotecaForm(forms.Form):
    artista = forms.CharField(max_length=50)
    disco = forms.CharField(max_length=50)
    cantidad_canciones = forms.IntegerField(label="cantidad_canciones")
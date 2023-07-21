from django import forms
from .models import Noticia


class Form_Alta(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('titulo','descripcion','contenido','imagen','categoria')


class Form_Modificacion(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('titulo', 'descripcion', 'contenido', 'imagen', 'categoria')
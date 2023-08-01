from django import forms
from .models import Noticia, Categoria


class Form_Alta(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'descripcion', 'contenido', 'imagen', 'categoria')
        widgets = {
            'categoria': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
                'type': 'checkbox', 
                'value': '',
                'id':'defaultCheck1',
            }),
             
        }


class Form_Modificacion(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('titulo', 'descripcion', 'contenido', 'imagen', 'categoria')
        widgets = {
            'categoria': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
                'type': 'checkbox', 
                'value': '',
                'id':'defaultCheck1',
            })
        }

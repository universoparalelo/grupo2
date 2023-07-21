from django.shortcuts import render
from apps.noticias.models import Noticia


def Inicio(request):
	ctx = {}
	lista_noticias = Noticia.objects.all()
	ctx['object_list'] = lista_noticias
	return render(request, 'inicio.html', ctx)


def SobreNosotros(request):
	return render(request,'sobre-nosotros.html')


def Contacto(request):
	return render(request,'contacto.html')




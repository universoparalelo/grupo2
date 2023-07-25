from django.shortcuts import render
from apps.noticias.models import Noticia


def Inicio(request):
	ctx = {}
	lista_noticias = Noticia.objects.order_by('-creado')
	ctx['object_list'] = lista_noticias[0:3]
	ctx['sola'] = lista_noticias[3]
	ctx['otras'] = lista_noticias[4:9] 
	return render(request, 'inicio.html', ctx)


def SobreNosotros(request):
	return render(request,'sobre-nosotros.html')


def Contacto(request):
	return render(request,'contacto.html')


def OrdFechaDesc(request):
	ctx = {}
	lista_noticias = Noticia.objects.order_by('creado')
	ctx['object_list'] = lista_noticias[0:6]
	return render(request, 'ord-fecha-desc.html', ctx)


def OrdTitAsc(request):
	ctx = {}
	lista_noticias = Noticia.objects.order_by('titulo')
	ctx['object_list'] = lista_noticias[0:6]
	return render(request, 'ord-tit-asc.html', ctx)


def OrdTitDesc(request):
	ctx = {}
	lista_noticias = Noticia.objects.order_by('-titulo')
	ctx['object_list'] = lista_noticias[0:6]
	return render(request, 'ord-tit-desc.html', ctx)


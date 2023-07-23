from django.shortcuts import render, HttpResponseRedirect
from apps.noticias.models import Noticia
from apps.comentarios.models import Comentario
from django.views.generic import DeleteView, UpdateView
from .forms import Form_Modificacion

from django.urls import reverse_lazy


def Agregar(request,pk):
	#OBTENER DATOS A GUARDAR
	com = request.POST.get('comentario', None)
	usuario = request.user
	noticia = Noticia.objects.get(id = pk)

	Comentario.objects.create(texto = com, usuario = usuario, noticia = noticia)

	return HttpResponseRedirect(reverse_lazy('noticias:detalle_noticia' , kwargs={'pk':pk}))

class BorrarComentario(DeleteView):
	model = Comentario
	success_url = reverse_lazy('noticias:misNoticias')
	

class ModificarComentario(UpdateView):
	model = Comentario
	form_class = Form_Modificacion
	template_name = 'noticias/modificar.html'
	success_url = reverse_lazy('noticias:misNoticias')
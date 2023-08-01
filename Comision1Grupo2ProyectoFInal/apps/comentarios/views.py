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
	permission_required = 'comentarios.delete_comentario'
	def get_success_url(self):        
		return reverse_lazy('noticias:detalle_noticia',kwargs={'pk': self.object.noticia.pk})
	

class ModificarComentario(UpdateView):
	model = Comentario
	form_class = Form_Modificacion
	template_name = 'comentarios/modificar.html'
	permission_required = 'comentarios.change_noticia'

	def get_success_url(self):        
		return reverse_lazy('noticias:detalle_noticia',kwargs={'pk': self.object.noticia.pk})


def MisComentarios(request):
	ctx={}

	misComentarios = Comentario.objects.filter(usuario_id = request.user).order_by('-creado')
	listaCom = []

	for com in misComentarios:
		nuevoCom = Noticia.objects.get(id = com.noticia_id)
		listaCom.append(nuevoCom)

	ctx['com'] = listaCom
	
	return render(request, 'comentarios/misComentarios.html', ctx)

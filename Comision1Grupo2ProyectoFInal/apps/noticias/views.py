from django.shortcuts import render
from .models import Categoria, Noticia
from apps.comentarios.models import Comentario
from .forms import *
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

#CONTROLA SI EL USUARIO ESTA LOGEADO
from django.contrib.auth.mixins import LoginRequiredMixin

#Permisos de colaborador
from django.contrib.auth.mixins import PermissionRequiredMixin

#Handler de errores
from django.core.exceptions import PermissionDenied
# Create your views here.

def Categorias(request):
    ctx = {}

    objetos_categorias = Categoria.objects.all()

    ctx['object_list'] = objetos_categorias

    return render(request, 'noticias/categorias.html', ctx)



# class CrearNoticia(PermissionRequiredMixin, CreateView):
class CrearNoticia( CreateView):
	model = Noticia
	form_class = Form_Alta
	template_name = 'noticias/crearNoticia.html'
	success_url = reverse_lazy('noticias:misNoticias')
	permission_required = 'noticias.add_noticia'

	def form_valid(self, form):
		noticia = form.save(commit=False)
		noticia.autor = self.request.user
		return super(CrearNoticia, self).form_valid(form)
	
    
def MisNoticias(request):
	ctx = {}
	lista_noticias = Noticia.objects.filter(autor = request.user).order_by('-creado')
	print(lista_noticias)
	ctx['object_list'] = lista_noticias

	return render(request, 'noticias/misNoticias.html', ctx)


def ListarNoticias(request):
	ctx = {}
	categorias = Categoria.objects.all()
	#CAPUTRAR PARAMETROS
	todas_noticias = Noticia.objects.all()
	orden = request.GET.get('orden',None)
	if orden:
		if orden == 'titulo_desc':
			todas_noticias = todas_noticias.order_by('-titulo')
		elif orden == 'titulo_asc':
			todas_noticias = todas_noticias.order_by('titulo')
		elif orden == 'noti_nuevas':
			todas_noticias = todas_noticias.order_by('-creado')
		elif orden == 'noti_viejas':
			todas_noticias = todas_noticias.order_by('creado')

	ctx['object_list'] = todas_noticias
	return render(request, 'noticias/listarNoticias.html', ctx)



class BorrarNoticia(PermissionRequiredMixin,DeleteView):
	model = Noticia
	success_url = reverse_lazy('noticias:misNoticias')
	permission_required = 'noticias.delete_noticia'
	permission_denied_message = 'NO ESTAS AUTORIZADO PARA REALIZAR CAMBIOS '

#probando permisos de colaborador para editar 

class ModificarNoticia(PermissionRequiredMixin,UpdateView):
	model = Noticia
	form_class = Form_Modificacion
	template_name = 'noticias/modificar.html'
	success_url = reverse_lazy('noticias:misNoticias')
	permission_required = 'noticias.change_noticia'
	permission_denied_message = 'NO ESTAS AUTORIZADO PARA REALIZAR CAMBIOS'
	

def DetalleNoticia(request, pk):
	ctx = {}
	mis_com = []

	detalle_noticia = Noticia.objects.get(id = pk)
	comentarios = Comentario.objects.filter(noticia = pk).order_by('-creado')
	
	ctx['detalle'] = detalle_noticia
	ctx['lista_comentarios'] = comentarios

	return render(request, 'noticias/detalle.html', ctx)


def NoticiasPorCategoria(request, pk):
	# pk de la categoria
	ctx = {}
	orden = request.GET.get('orden',None)
	noticias = Noticia.objects.filter(categoria = pk)
	categoria = Categoria.objects.get(id = pk)
	if orden:
		if orden == 'titulo_desc':
			noticias = noticias.order_by('-titulo')
		elif orden == 'titulo_asc':
			noticias = noticias.order_by('titulo')
		elif orden == 'noti_nuevas':
			noticias = noticias.order_by('-creado')
		elif orden == 'noti_viejas':
			noticias = noticias.order_by('creado')

	ctx['noticia'] = noticias
	ctx['nom_cat'] = categoria

	return render(request, 'noticias/noticiasPorCat.html', ctx)
	


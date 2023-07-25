from django.shortcuts import render
from .models import Categoria, Noticia
from apps.comentarios.models import Comentario
from .forms import *
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

#CONTROLA SI EL USUARIO ESTA LOGEADO
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def Categorias(request):
    ctx = {}

    objetos_categorias = Categoria.objects.all()

    ctx['object_list'] = objetos_categorias

    return render(request, 'noticias/categorias.html', ctx)



class CrearNoticia(LoginRequiredMixin, CreateView):
	model = Noticia
	form_class = Form_Alta
	template_name = 'noticias/crearNoticia.html'
	success_url = reverse_lazy('noticias:misNoticias')

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
    noticias = Noticia.objects.all()
    ctx['object_list'] = noticias

    return render(request, 'noticias/listaNoticias.html', ctx)


class BorrarNoticia(DeleteView):
	model = Noticia
	success_url = reverse_lazy('noticias:misNoticias')
	

class ModificarNoticia(UpdateView):
	model = Noticia
	form_class = Form_Modificacion
	template_name = 'noticias/modificar.html'
	success_url = reverse_lazy('noticias:misNoticias')
	

def DetalleNoticia(request, pk):
	ctx = {}

	detalle_noticia = Noticia.objects.get(id = pk)
	comentarios = Comentario.objects.filter(noticia = pk).order_by('-creado')

	ctx['detalle'] = detalle_noticia
	ctx['lista_comentarios'] = comentarios

	return render(request, 'noticias/detalle.html', ctx)


def NoticiasPorCategoria(request, pk):
	# pk de la categoria
	ctx = {}
	
	ctx['noticia'] = Noticia.objects.filter(categoria = pk)
	ctx['nom_cat'] = Categoria.objects.get(id = pk)

	return render(request, 'noticias/noticiasPorCat.html', ctx)
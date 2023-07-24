from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
	nombre = models.CharField(max_length=80)
	imagen_cat = models.ImageField(upload_to = 'categorias', default='https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2017/12/04-11-2017-IFAD-35822.jpg')

	def __str__(self):
		return self.nombre

#########################################################################

class Noticia(models.Model):
	creado = models.DateTimeField(
		'creado',
		auto_now_add=True
	)
	modificado = models.DateTimeField(
		'modificado',
		auto_now=True
	)
	titulo = models.CharField(max_length = 250)
	descripcion = models.CharField(max_length= 400)
	contenido = models.TextField()
	autor = models.ForeignKey(User, on_delete = models.CASCADE)
	imagen = models.ImageField(upload_to = 'noticias')
	categoria = models.ManyToManyField(Categoria, blank=False)

	def __str__(self):
		return self.titulo
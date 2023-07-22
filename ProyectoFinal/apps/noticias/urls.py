from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    # Ver categorias
    path('categorias', views.Categorias, name="categorias"),

    # Crear una noticia
    path('crearNoticia', views.CrearNoticia.as_view(), name = 'crearNoticia'),

    # Noticias del usuario 
    path('mis-noticias', views.MisNoticias, name="misNoticias"),

    # Listar noticias
    path('listar-noticias', views.ListarNoticias, name='listar_noticias'),

    # Borrar una noticia
    path('borrar-noticia/<int:pk>', views.BorrarNoticia.as_view(), name="borrar_noticia"),

    # Actualizar una noticia
    path('modificar-noticia/<int:pk>', views.ModificarNoticia.as_view(), name="modificar_noticia"),

    # Detalle de una noticia
    path('detalle-noticia/<int:pk>', views.DetalleNoticia, name='detalle_noticia'),

    # Noticias por categoria
    path('not-categoria/<int:pk>', views.NoticiasPorCategoria, name='not_categoria'),
]
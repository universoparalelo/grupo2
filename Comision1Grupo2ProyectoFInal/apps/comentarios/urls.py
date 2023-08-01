from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
    # Agregar comentario
    path('agregar-com/<int:pk>', views.Agregar, name='agregar_comentarios'),

    # Modificar comentario
    path('borrar-comentario/<int:pk>', views.BorrarComentario.as_view(), name="borrar_comentario"),

    # Borrar comentario
    path('modificar-comentario/<int:pk>', views.ModificarComentario.as_view(), name="modificar_comentario"),

    # Seccion mis comentarios
    path('mis-comentarios', views.MisComentarios, name='misComentarios'),

]
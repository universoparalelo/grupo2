from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
    # Agregar comentario
    path('agregar-com/<int:pk>', views.Agregar, name='agregar_comentarios'),
]
from django.urls import path
from .views import *

urlpatterns = [
    
    #path('lista-cursos/', lista_cursos),
    path('', inicio),
    path('vecinos/',vecinos, name='Vecinos'),
    path('instalaciones/',instalaciones, name='Instalaciones'),
    path('provedores/',provedores, name='Provedores'),
    path('vecino-formulario/', vecino_formulario, name='VecinoFormulario'),
    path('agrega-vecino/<nombre>/<domicilio>', crea_vecino),
    path('provedor-formulario/', provedor_formulario, name='ProvedorFormulario'),
    #path('entregables/', entregables, name='Entregables'),
    #path('curso-formulario/', curso_formulario, name='CursoFormulario'),
    #path('busqueda-camada/', busqueda_camada, name='BusquedaCamada'),
    #path('buscar-camada/', buscar_camada, name='BuscarCamada'),
]
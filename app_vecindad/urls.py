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
    path('lista-vecinos/', lista_vecinos),
    path('busqueda-servicio/', busqueda_servicio, name='BusquedaServicio'),
    path('buscar-servicio/', buscar_servicio, name='BuscarServicio'),
]
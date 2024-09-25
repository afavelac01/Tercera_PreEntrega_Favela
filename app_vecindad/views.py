from django.shortcuts import render
from django.http import HttpResponse
from .models import Vecino, Instalacion, Provedor
from .forms import VecinoFormulario, ProvedorFormulario

# Create your views here.


def crea_vecino(req, nombre, domicilio):
    nuevo_vecino = Vecino(nombre=nombre, domicilio=domicilio)
    nuevo_vecino.save()

    return HttpResponse(f"""
    <p>Vecino: {nuevo_vecino.nombre} - Servicio {nuevo_vecino.servicio} creado con éxito!</p>
  """)

def crea_provedor(req, nombre, domicilio, precio_base):
    nuevo_provedor = Provedor(nombre=nombre, domicilio=domicilio)
    nuevo_provedor.save()

    return HttpResponse(f"""
    <p>Vecino: {nuevo_provedor.nombre} - Servicio {nuevo_provedor.servicio} - Domiclio {nuevo_provedor.precio_base}creado con éxito!</p>
  """)




def inicio(req):

  return render(req, "inicio.html", {})


def vecinos(req):

  return render(req, "vecinos.html", {})

def instalaciones(req):

  return render(req, "instalaciones.html", {})

def provedores(req):

  return render(req, "instalaciones.html", {})

def vecino_formulario(req):

  print('method', req.method)
  print('data', req.POST)

  if req.method == 'POST':

    mi_formulario = VecinoFormulario(req.POST)

    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data

      nuevo_vecino = Vecino(nombre=data["vecino"], domicilio=data["domicilio"])
      nuevo_vecino.save()

      return render(req, "inicio.html", {})
    
    else:
      return render(req, "vecino_formulario.html", { "mi_formulario": mi_formulario })
  
  else:

    mi_formulario = VecinoFormulario()
    return render(req, "vecino_formulario.html", { "mi_formulario": mi_formulario })
  
def provedor_formulario(req):

  if req.method == 'POST':

    mi_formulario = ProvedorFormulario(req.POST)

    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data

      nuevo_provedor = Provedor(nombre=data["provedor"], servicio=data["servicio"], precio_base=data["precio_base"])
      nuevo_provedor.save()

      return render(req, "inicio.html", {})
    
    else:
        return render(req, "provedor_formulario.html", { "mi_formulario": mi_formulario })
  
  else:

    mi_formulario = ProvedorFormulario()
    return render(req, "provedor_formulario.html", { "mi_formulario": mi_formulario })
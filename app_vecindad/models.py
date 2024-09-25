from django.db import models

# Create your models here.
class Vecino(models.Model):

  nombre = models.CharField(max_length=30)
  domicilio = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.nombre} - {self.domicilio}'

class Instalacion(models.Model):

  nombre = models.CharField(max_length=30)
  costo = models.FloatField()

  def __str__(self):
    return f'{self.nombre} - {self.costo}'

class Provedor(models.Model):

  nombre = models.CharField(max_length=30)
  servicio = models.CharField(max_length=30)
  precio_base = models.FloatField()

  def __str__(self):
    return f'{self.nombre} - {self.servicio}'
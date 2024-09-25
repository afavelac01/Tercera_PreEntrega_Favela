from django.contrib import admin
from .models import Vecino, Instalacion, Provedor

# Register your models here.
admin.site.register(Vecino)
admin.site.register(Instalacion)
admin.site.register(Provedor)

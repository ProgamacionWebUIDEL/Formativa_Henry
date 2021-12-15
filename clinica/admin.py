from django.contrib import admin

#from clinica_veterinaria.clinica.models import Mascotas
from django.contrib import admin

from .models import Accesorios, Mascotas

# Register your models here.
admin.site.register(Mascotas)
admin.site.register(Accesorios)
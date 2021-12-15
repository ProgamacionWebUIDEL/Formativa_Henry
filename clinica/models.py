from django.db import models

# Create your models here.
class Mascotas(models.Model):
    nombre=models.CharField(max_length=120, help_text='Nombre de la Mascota')
    tipo_mascota=models.CharField(max_length=120, help_text='Tipo de  Mascota')
    raza=models.CharField(max_length=120, help_text='Raza de la Mascota')
    edad=models.IntegerField(max_length=120, help_text='Edad de la Mascota')

class Accesorios(models.Model):
    nombre=models.CharField(max_length=120, help_text='Nombre del Accesorio')
    cantidad=models.IntegerField(max_length=120, help_text='Cantidad de Accesorios')
    valor=models.FloatField(max_length=120, help_text='Valor del Accesorio')

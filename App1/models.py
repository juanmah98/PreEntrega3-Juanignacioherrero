from django.db import models

# Create your models here.
class prodcutos(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    talle = models.IntegerField()
    color = models.CharField(max_length=30)

class contacto(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    telefono = models.IntegerField()
    mensaje = models.TextField(max_length=2000)

class devolucion(models.Model):
    numero_orden = models.IntegerField()
    fecha_compra = models.DateField()
    telefono = models.IntegerField()
    nombre_apellido = models.CharField(max_length=30)
    prendas_motivo = models.TextField(max_length=400) 
    domicilio = models.CharField(max_length=40)


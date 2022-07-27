from django.db import models

# Create your models here.

class Estudiantes(models.Model):
    codigo= models.IntegerField()
    dni= models.IntegerField()
    nombre= models.TextField()
    apepat = models.TextField()
    apemat = models.TextField()
    direccion = models.TextField()
    telefono = models.IntegerField()
    estado = models.BooleanField()
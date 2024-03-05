from django.db import models

# Create your models here.

class Calificaciones(models.Model):
    nombre_profesor = models.CharField(max_length=200)
    materia = models.TextField(max_length=100)
    calificacion = models.TextField(max_length=3)
    fecha = models.DateField()

    def __str__(self): return self.nombre_profesor
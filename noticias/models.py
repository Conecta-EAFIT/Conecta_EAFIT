from django.db import models
from profesor.models import Profesor

# Create your models here.
class Noticias(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
    author = models.ManyToManyField(Profesor, related_name='noticias', blank=True)

    def __str__(self): return self.headline

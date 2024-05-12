from django.db import models
from profesor.models import Profesor

# Create your models here.
class Noticias(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
    author = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, related_name='noticias')

    def __str__(self): return self.headline

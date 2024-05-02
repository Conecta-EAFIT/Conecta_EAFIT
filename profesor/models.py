from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Carrera(models.Model):
    name_carreer = models.CharField(max_length=100)

    def __str__(self):
        return self.name_carreer
    
    
class Profesor(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='profesor/images/', default='profesor/images/defaultt.jpg')
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)
    carreers = models.ManyToManyField(Carrera, related_name='profesores', blank=True)
    
    
    def __str__(self):
        return self.title




class Voto(models.Model):
    valor = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)  # Suponiendo que tienes un modelo Profesor

    class Meta:
        unique_together = ['usuario', 'profesor']  # Esto garantiza que un usuario solo pueda votar una vez por cada profesor


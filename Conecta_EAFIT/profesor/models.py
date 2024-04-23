from django.db import models

# Create your models here.
class Carrera(models.Model):
    name_carreer = models.CharField(max_length=100)

    def __str__(self):
        return self.name_carreer
    
    
class Profesor(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='profesor/images/')
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    carreers = models.ManyToManyField(Carrera, related_name='profesores', blank=True)
    
    
    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
# Create your models here.
class Carrera(models.Model):
    name_carreer = models.CharField(max_length=100)

    def __str__(self):
        return self.name_carreer
    
    
class Profesor(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    description = models.TextField(blank=True, validators=[MinLengthValidator(120)])
    image = models.ImageField(upload_to='profesor/images/', default='profesor/images/defaultt.jpg')
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.DateField(blank=True, null=True)
    carreers = models.ManyToManyField(Carrera, related_name='profesores', blank=True)
    education = models.TextField(blank=True)
    

    def __str__(self):
        return self.title




class Voto(models.Model):
    valor = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)  # Suponiendo que tienes un modelo Profesor

    class Meta:
        unique_together = ['usuario', 'profesor']  # Esto garantiza que un usuario solo pueda votar una vez por cada profesor

class Comentario(models.Model):
    texto = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['usuario', 'profesor']  # Un usuario solo puede comentar una vez por profesor
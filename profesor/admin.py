from django.contrib import admin
from .models import Profesor, Carrera, Comentario, Voto



# Register your models here.
admin.site.register(Profesor)
admin.site.register(Carrera)
admin.site.register(Comentario)
admin.site.register(Voto)


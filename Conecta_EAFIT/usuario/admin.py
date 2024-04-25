from django.contrib import admin
from .models import User, Administrador, Estudiante


admin.site.register(Administrador)
admin.site.register(Estudiante)

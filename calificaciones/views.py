from django.shortcuts import render
from .models import Calificaciones
# Create your views here.

def calificaciones(request):
    calificacioness = Calificaciones.objects.all().order_by('-fecha')
    return render(request, 'calificaciones.html', {'calificacioness':calificacioness})

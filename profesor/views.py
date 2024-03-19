from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Profesor

def _profesores(request):
    searchTerm = request.GET.get('searchProfesor')
    if searchTerm:
        profesores = Profesor.objects.filter(title__icontains=searchTerm)
    else:
        profesores = Profesor.objects.all()
    return render(request, 'profesores.html', {'searchTerm':searchTerm, 'profesores': profesores})

def _conectaHome(request):
    return render (request, 'conectaHome.html')


def _about(request):
    return render(request, 'about.html')
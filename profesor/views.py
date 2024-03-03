from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Profesor

def home(request):
    searchTerm = request.GET.get('searchProfesor')
    if searchTerm:
        profesores = Profesor.objects.filter(title__icontains=searchTerm)
    else:
        profesores = Profesor.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'profesores': profesores})


def about(request):
    return HttpResponse('<h1> Welcome to About Page </h1>')
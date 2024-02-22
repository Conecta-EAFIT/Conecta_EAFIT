from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Profesor

def home(request):
    searchTerm = request.GET.get('searchProfesor')
    if searchTerm:
        profesor = Profesor.objects.filter(title__icontains=searchTerm)
    else:
        profesor = Profesor.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'profesor': profesor})


def about(request):
    return render(request, 'about.html')
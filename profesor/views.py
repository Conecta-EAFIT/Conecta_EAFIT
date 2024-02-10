from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Jose Duque'})

def about(request):
    return HttpResponse('<h1>Bienvenido a la About Page</h1>')
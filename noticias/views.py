from django.shortcuts import render
from .models import Noticias
# Create your views here.

def noticias(request):
    noticiass = Noticias.objects.all().order_by('-date')
    return render(request, 'noticias.html', {'noticiass':noticiass})
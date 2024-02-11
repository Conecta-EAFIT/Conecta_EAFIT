from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html', {'name': 'Greg Lim'})
# Create your views here.
def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')
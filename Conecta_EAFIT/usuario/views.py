from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Administrador, Estudiante

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Verificar el tipo de usuario
            if Administrador.objects.filter(usuario=user).exists():
                return redirect('profesor:conectaHome_admin')
            elif Estudiante.objects.filter(usuario=user).exists():
                return redirect('profesor:conectaHome')
            else:
                # Manejar otros tipos de usuarios si es necesario
                pass
        else:
            # Manejar autenticación fallida
            pass
    return render(request, 'login.html')

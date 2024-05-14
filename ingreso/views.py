from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from usuario.models import Administrador, Estudiante

# Create your views here.
def home1(request):
    #messages.get_messages(request)
    return render(request, "home1.html")

def signup(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        myuser = User.objects.create_user(username, email, password1)
        myuser.save()

        messages.success(request, "Tu cuenta se ha creado correctamente. ")
        print("El usuario se ha registrado")
        return redirect('login')

    return render(request, "signup.html")

def login(request):
    print("Se esta ejecutando la funcion login()")
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        # if user is not None:
        #     username = user.username
        #     return redirect('conectaHome')
        # else:
        #     #messages.error(request, "Los datos ingresados son inválidos")
        #     return redirect('home1')
        if user is not None:
            auth_login(request, user)
            print("El usuario se ha logueado")
            estudiante, creado = Estudiante.objects.get_or_create(usuario=user, defaults={'nombre': user.username, 'email': user.email})
            return redirect('conectaHome')
        else:
            messages.error(request, "Los datos ingresados son inválidos")
            return redirect('home1')
    return render(request, "login.html")

def signout(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente")
    print("Se cerró la sesión")
    return redirect('home1')


def menu(request):
    messages.get_messages(request)
    return render(request, "profesor/home.html")
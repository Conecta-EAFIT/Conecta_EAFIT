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
        return redirect('login')

    return render(request, "signup.html")

def login(request):
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
            # if user is not None:
            #     #username = user.username
            #     return redirect('conectaHome')
            # else:
            #     messages.error(request, "Los datos ingresados son inválidos")
            #     return redirect('home1')
            user = authenticate(username=username, password=password1)

            if user is not None:
                auth_login(request, user)
                if hasattr(user, 'administrador'):
                    # El usuario es un administrador
                    print("El usuario es un administrador.")
                elif hasattr(user, 'estudiante'):
                    # El usuario es un estudiante
                    print("El usuario es un estudiante.")
                else:
                    # El usuario no tiene perfil de administrador ni de estudiante
                    messages.error(request, "Los datos ingresados son inválidos")
                    print("El usuario no tiene perfil de administrador ni de estudiante.")
            else:
                # La autenticación falló
                print("La autenticación falló.")

        else:
            messages.error(request, "Los datos ingresados son inválidos")
        return redirect('home1')
    return render(request, "login.html")

def signout(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente")
    return redirect('home1')


def menu(request):
    messages.get_messages(request)
    return render(request, "profesor/home.html")
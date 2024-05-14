from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Voto, Comentario
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import get_object_or_404

# Create your views here.

from .models import Profesor, Carrera

def _profesores(request):
    searchTerm = request.GET.get('searchProfesor')
    searchTerm1 = request.GET.get('searchProfesor1')
    if searchTerm:
        profesores = Profesor.objects.filter(title__icontains=searchTerm)
    elif searchTerm1:
        profesores = Profesor.objects.filter(carreers__name_carreer__icontains=searchTerm1)
    else:
        profesores = Profesor.objects.all()
    return render(request, 'profesores.html', {'searchTerm': searchTerm, 'searchTerm1': searchTerm1, 'profesores': profesores})

def conectaHome(request):
    return render (request, 'conectaHome.html')

def _about(request):
    return render(request, 'about.html')

def profesor_por_carrera(request, carrera_id):
    carrera = Carrera.objects.get(nombre=carrera_id)
    Profesor = Carrera.objects.filter(Carrera=carrera)
    return render(request, 'home.html', {'carrera': carrera, 'Profesor': Profesor})

def customer_record(request, pk):
	if request.user.is_authenticated:
		Profesores = Profesor.objects.get(id=pk)
		return render(request, 'record.html', {'Profesor': Profesores})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('conectaHome')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Profesor.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Profesor elimnado Correctamente...")
		return redirect('profesores')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")


def add_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddRecordForm(request.POST, request.FILES)
            if form.is_valid():
                print("El formato ha sido diligenciado correctamente")
                form.save()
                messages.success(request, "Registro añadido exitosamente.")
                return redirect('conectaHome')
            else:
                print("El formato NO FUE diligenciado correctamente")
                messages.error(request, "* Hubo un error en el diligenciamiento. Revisa todos los campos.")
                messages.error(request, "* Min de caracteres: 120")
                messages.error(request, "* El correo debe terminar en un dominio (.com, .co, etc) y debe tener @")
        else:
            form = AddRecordForm()
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('conectaHome')

def update_record(request, pk):
    current_record = Profesor.objects.get(id=pk)
    if request.method == 'POST':
        form = AddRecordForm(request.POST, request.FILES, instance=current_record)
        if form.is_valid():
            form.save()
            print("Se actualizó el profesor...........") 
            messages.success(request, "El Profesor se ha actualizado correctamente!")
            return redirect('conectaHome')
    else:
        form = AddRecordForm(instance=current_record)
    return render(request, 'update_record.html', {'form': form})

@login_required
def plantillaProfesor(request, pk, nombreP):
    profesor = Profesor.objects.get(id=pk, title=nombreP)
    usuario = request.user

    usuario = request.user
    profesor = get_object_or_404(Profesor, title=nombreP)
    promedio_votos = Voto.objects.filter(profesor=profesor).aggregate(Avg('valor'))['valor__avg']

    voto_usuario = None
    nuevo_comentario =None
    if Voto.objects.filter(usuario=usuario, profesor=profesor).exists():
        voto_usuario = Voto.objects.get(usuario=usuario, profesor=profesor).valor

    if request.method == 'POST':
        if 'voto' in request.POST:  # Verificar si se envió un voto
            if not Voto.objects.filter(usuario=request.user, profesor=profesor).exists():
                valor_voto = int(request.POST['voto'])
                voto = Voto.objects.create(usuario=request.user, profesor=profesor, valor=valor_voto)
                promedio_votos = round(Voto.objects.filter(profesor=profesor).aggregate(Avg('valor'))['valor__avg'], 1)
                voto_usuario = valor_voto  # Actualiza el voto del usuario después de votar
        elif 'texto' in request.POST:  # Verificar si se envió un comentario
            texto_comentario = request.POST.get('texto')
            comentario_existente = Comentario.objects.filter(usuario=request.user, profesor=profesor).exists()

            if not comentario_existente:
                nuevo_comentario = Comentario.objects.create(texto=texto_comentario, usuario=request.user,profesor=profesor)

    comentarios = Comentario.objects.filter(profesor=profesor)

    return render(request, 'plantillaProfesor.html', {
        'profesor': profesor,
        'voto_usuario': voto_usuario,
        'promedio_votos': promedio_votos,
        'comentarios': comentarios,  # Pasar todos los comentarios del profesor a la plantilla
        'nuevo_comentario': nuevo_comentario
    })
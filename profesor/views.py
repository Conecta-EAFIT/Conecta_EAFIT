from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Voto
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

def conectaHome_admin(request):
    return render (request, 'conectaHome_admin.html')


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
		messages.success(request, "Record Deleted Successfully...")
		return redirect('_profesores')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")


def add_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddRecordForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect('Conectahome')
        else:
            form = AddRecordForm()
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('conectaHome')

def update_record(request, pk):
    current_record = Profesor.objects.get(id=pk)
    if request.method == 'POST':
        form = AddRecordForm(request.POST, request.FILES, instance=current_record)
        if form.is_valid():
            form.save() 
            messages.success(request, "Record Has Been Updated!")
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
    if Voto.objects.filter(usuario=usuario, profesor=profesor).exists():
        voto_usuario = Voto.objects.get(usuario=usuario, profesor=profesor).valor

    if request.method == 'POST':
        if not Voto.objects.filter(usuario=usuario, profesor=profesor).exists():
            valor_voto = int(request.POST['voto'])
            voto = Voto.objects.create(usuario=usuario, profesor=profesor, valor=valor_voto)
            promedio_votos = Voto.objects.filter(profesor=profesor).aggregate(Avg('valor'))['valor__avg']
            voto_usuario = valor_voto  # Actualiza el voto del usuario después de votar

    return render(request, 'plantillaProfesor.html',
                  {'profesor': profesor, 'voto_usuario': voto_usuario, 'promedio_votos': promedio_votos})

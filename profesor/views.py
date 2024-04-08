from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
# Create your views here.

from .models import Profesor, Carrera

def _profesores(request):
    searchTerm = request.GET.get('searchProfesor')
    if searchTerm:
        profesores = Profesor.objects.filter(title__icontains=searchTerm)
    else:
        profesores = Profesor.objects.all()
    return render(request, 'profesores.html', {'searchTerm':searchTerm, 'profesores': profesores})

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
		messages.success(request, "Record Deleted Successfully...")
		return redirect('conectaHome')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('conectaHome')


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

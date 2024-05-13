from django.shortcuts import render, redirect
from .models import Noticias
from .forms import SignUpForm, AddNoticiaForm
from django.contrib import messages
# Create your views here.

def noticias(request):
    noticias = Noticias.objects.all().order_by('-date')
    return render(request, 'noticias.html', {'noticias':noticias})


def add_noticias(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddNoticiaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect('conectaHome')
        else:
            form = AddNoticiaForm()
        return render(request, 'add_noticias.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('conectaHome')
    
def customer_noticias(request, pk):
	if request.user.is_authenticated:
		Profesores = Noticias.objects.get(id=pk)
		return render(request, 'record.html', {'Profesor': Profesores})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('conectaHome')



def delete_noticias(request, pk):
	if request.user.is_authenticated:
		delete_it = Noticias.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('profesores')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
            
def update_noticias(request, pk):
    current_record = Noticias.objects.get(id=pk)
    if request.method == 'POST':
        form = AddNoticiaForm(request.POST, request.FILES, instance=current_record)
        if form.is_valid():
            form.save() 
            messages.success(request, "Record Has Been Updated!")
            return redirect('conectaHome')
    else:
        form = AddNoticiaForm(instance=current_record)
    return render(request, 'update_noticias.html', {'form': form})

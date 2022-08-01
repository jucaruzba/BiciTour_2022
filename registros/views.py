from django.shortcuts import render
from .forms import ComentarioUserForm, FormArchivos
from .models import ComentarioUsuario, Tours, Archivos
from django.contrib import messages

def registros(request):
    tours=Tours.objects.all()
    return render(request, "registros/principal.html",{'tours': tours})

def registros2(request):
    tours=Tours.objects.all()
    return render(request, 'registros/tours.html',{'tours': tours})

def registros3(request):
    archivos=Archivos.objects.raw('SELECT id, nombre, email, mensaje, archivo FROM registros_archivos ORDER BY nombre DESC')
    return render(request, 'registros/archivos.html', {'archivos': archivos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioUserForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'registros/archivos.html')
    form = ComentarioUserForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/archivos.html',{'form': form}) 


def archivos(request):
    
    if request.method == 'POST':
        
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            nombre =request.POST['nombre']
            mensaje =request.POST['mensaje']
            email =request.POST['email']
            archivo =request.FILES['archivo']
            insert = Archivos(nombre=nombre, mensaje=mensaje, email=email, archivo=archivo)
            insert.save()
            archivos = Archivos.objects.all()
            return render(request, 'registros/experiences.html', {'archivos': archivos})
        else:
            messages.error(request, 'Error al subir el archivo')
    else:
        return render(request, 'registros/archivos.html', {'archivo':Archivos})

def consultasSQL(request):
    archivos=Archivos.objects.raw('SELECT id, nombre, email, mensaje, archivo FROM registros_archivos ORDER BY nombre DESC')
    return render (request, 'registros/archivos.html', {'archivos':archivos})

def experiencias(request):
    archivos=Archivos.objects.all()
    return render(request, 'registros/experiences.html',{'archivos': archivos})
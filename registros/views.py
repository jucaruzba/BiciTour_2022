from django.shortcuts import render

from .forms import ComentarioUserForm

from .models import ComentarioUsuario, Tours

def registros(request):
    tours=Tours.objects.all()
    return render(request, "registros/principal.html",{'tours': tours})

def registros2(request):
    tours=Tours.objects.all()
    return render(request, 'registros/tours.html',{'tours': tours})

def registros3(request):
    form=ComentarioUsuario.objects.all()
    return render(request, 'registros/experiences.html', {'form': form})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioUserForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'registros/experiences.html')
    form = ComentarioUserForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/experiences.html',{'form': form}) 
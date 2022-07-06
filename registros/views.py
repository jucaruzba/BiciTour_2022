from django.shortcuts import render

from .models import Tours

def registros(request):
    tours=Tours.objects.all()
    return render(request, "registros/principal.html",{'tours': tours})

def registros2(request):
    tours=Tours.objects.all()
    return render(request, 'registros/tours.html',{'tours': tours})

def registros3(request):
    tours=Tours.objects.all()
    return render(request, 'registros/experiences.html', {'tours': tours})
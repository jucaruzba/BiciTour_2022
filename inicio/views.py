from django.shortcuts import render

def principal(request):
    return render(request, 'inicio/principal.html')

def tours(request):
    return render(request, 'inicio/tours.html')

def experiences(request):
    return render(request, 'inicio/experiences.html')

def contact(request):
    return render(request, 'inicio/contact.html')

def about(request):
    return render(request, 'inicio/about.html')
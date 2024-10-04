# myapp/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Specify app namespace

def about(request):
    return render(request, 'about.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def ethos(request):
    return render(request, 'ethos.html')

def key_skills(request):
    return render(request, 'key_skills.html')

def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

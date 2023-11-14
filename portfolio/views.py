from django.shortcuts import render
from .models import Project


def home(request):

    projects = Project.objects.all() #Obtiene los modelos de la base de datos

    return render(request, 'home.html', {'projects' : projects})

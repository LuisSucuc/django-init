from django.shortcuts import render
from .models import Persona


def inicio(request):
    personas = Persona.objects.all()
    context = { 'personas' : personas}
    return render(request, 'index.html', context)

def crearPersona(request):
    return render(request, 'crear_persona.html')
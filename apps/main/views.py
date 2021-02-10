from django.shortcuts import render
from .models import Persona


def inicio(request):
    personas = Persona.objects.all()
    print(personas)
    context = {personas: personas}
    return render(request, 'index.html', context)

# Create your views here.

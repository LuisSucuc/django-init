from django.contrib import admin
from .models import Persona

# Para que se puedan administrar desde el administrador
admin.site.register(Persona)

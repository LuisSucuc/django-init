
# Contenido HTML basado en un modelo
from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__' # ("name", "last_name", "email",) 
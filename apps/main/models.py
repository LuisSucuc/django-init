from django.db import models

# Create your models here.

class Persona(models.Model):
    id        = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=100)
    last_name = models.CharField(max_length=120)
    email     = models.EmailField(max_length=254)

    def __str__(self):
        #Por defecto muestra el nombre para cáda campo
        return self.name
    


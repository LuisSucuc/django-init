"""init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.main.views import inicio, crearPersona, editPersona, deletePersona
from apps.main.class_view import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete

urlpatterns = [
    path('admin/',                   admin.site.urls),
    path("",                         inicio,        name="index"),
    path("crear_persona/",           crearPersona,  name="crear_persona"),
    path("edit_persona/<int:id>/",   editPersona,   name="edit_persona"),
    path("delete_persona/<int:id>/", deletePersona, name="delete_persona"),

    path("index2",                      PersonaList.as_view(),   name="index2"),
    path("crear_persona2/",             PersonaCreate.as_view(), name="crear_persona2"),
    path("edit_persona2/<int:pk>/",     PersonaUpdate.as_view(), name="edit_persona2"),
    path("delete_persona2/<int:pk>/",   PersonaDelete.as_view(), name="delete_persona2"),
]

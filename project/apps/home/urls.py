from django.urls import path
from . import views

urlpatterns = [
    path ("",views.index, name="index"),
    path ("Añadir-personal/",views.añadir_personal, name="añadir-personal"),
    path ("Añadir-pais/",views.añadir_pais, name="añadir-pais"),
    path ("Añadir-sector/",views.añadir_sector, name="añadir-sector"),
]

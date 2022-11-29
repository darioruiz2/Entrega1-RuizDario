from CoderApp import views
from django.urls import path

urlpatterns = [
    path("", views.inicio, name = "inicio"),
    path("preceptores/", views.preceptores, name = "preceptores"),
    path("curso/",views.alumno, name = "alumno"),
    path("profesores/", views.profesores, name= "profesores"),
    path("busquedaAlumno/", views.busquedaAlumno, name = "busquedaAlumno"),
    path("buscar/",views.buscar, name = "buscar"),
]

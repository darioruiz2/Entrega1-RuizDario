from django.shortcuts import render
from .models import *
from .forms import * #importamos tanto nuestro models y nuestros forms con los cuales trabajaremos 

def inicio(request):
    return render(request, "AppCoder/inicio.html")


def preceptores(request):
    if request.method == "POST":
        form2 = preceptorForm(request.POST)
        if form2.is_valid():
            info2 = form2.cleaned_data
            nombreprece = info2["nombre"]
            emailprece = info2["email"]
            guardado3 = Preceptores(nombre = nombreprece, email = emailprece)
            guardado3.save()
            return render(request,"AppCoder/inicio.html")
    else:
        formulario3 = preceptorForm
    return render(request,"AppCoder/preceptores.html", {"form2": formulario3})

def alumno(request):
    if request.method == "POST":#aqui llegara el formulario mientras ejecute por el metodo post entrara al condicional ya con datos
        form = alumnoForm(request.POST)#guardamos el formulario en una variable llamada "form"
        print(form)#lo imprimimos para que nos lo muestre
        if form.is_valid():#Con este metodo validamos los datos de la variable "form"
            info = form.cleaned_data #vaciamos los datos pero antes los pasamos a otra variable
            nombrealumno = info["nombre"]#separamos los datos mediante diccionarios
            exptealumno = info["expte"]
            
            guardado1 = Alumno(nombre = nombrealumno,expte = exptealumno)
            guardado1.save()
            #Creamos la clase Alumno de los datos que teniamos de la variable "info" 
            # y luego guardamos en nuestra base de datos mediante el metodo .save()
            
            return render(request,"AppCoder/inicio.html")#De aqui nos mandamos a la pagina de inicio
    else:
        formulario = alumnoForm()#Pero si entramos por el metodo GET creamos un 
     #formulario vacio para llenarlo.
     #El view de profesores y preceptores es el mismo solo que con distintas variables y datos   
        
    return render(request,"AppCoder/alumno.html", {"form":formulario})
    

def profesores(request):
    
    if request.method == "POST": 
        form1 = profesoresForm(request.POST)
        if form1.is_valid():
            info1 = form1.cleaned_data
            nombreprofe = info1["nombre"]
            numeroprofe = info1["numero"]
            
            guardado2 = Profesores(nombre = nombreprofe, numero = numeroprofe)
            guardado2.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario2 = profesoresForm
    return render(request,"AppCoder/profesores.html", {"form1": formulario2})


def busquedaAlumno(request):
    return render(request, "AppCoder/BusquedaAlumno.html")
    #aqui creamos nuestro html de busqueda de alumnos

def buscar(request):
    if request.GET["expte"]:#mientras el get exista
        expediente = request.GET["expte"]#se va a almacenar en esta variable
        alumno = Alumno.objects.filter(expte = expediente)#traigo a una variable de un curso mediante
        #el metodo filter donde si mi expte es igual a la variable expediente 
        return render(request, "AppCoder/resultadobusqueda.html", {"alumno": alumno})#
        #renderizamos y nos dirigimos a una nueva view que se llamara resultadobusqueda
    else:#Este else solo se ejecutara si no introducimos ningun dato en nuestro formulario de busqueda de alumno 
        #y nos reedirigida a la vista de busqueda alumno agregando ese mensaje
        return render(request, "AppCoder/busquedaAlumno.html", {"mensaje": "No ingreso un alumno para buscar"})
    
    








from django.db import models
#Aqui los modelos que usaremos para los datos con los cuales trabajaremos
class Profesores(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    expte = models.IntegerField()
    
class Preceptores(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    


    


#Importamos modulos standars
import datetime
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Provincia(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.nombre

class Localidad(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='localidades')
    nombre = models.CharField(max_length=150, unique=True)
    #xpos VARCHAR(21)
    #ypos VARCHAR(21)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class Fotografia_localidad(models.Model):
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name='fotografias')
    imagen = models.FileField(upload_to='fotografias')
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = HTMLField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class Tipo_contenido(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.nombre

class Contenido(models.Model):
    localidad  = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name='contenidos')
    tipo_contenido  = models.ForeignKey(Tipo_contenido, on_delete=models.CASCADE, related_name='contenidos')
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = HTMLField(blank=True, null=True)
    direccion = models.CharField('Direccion', max_length=200, blank=True, null=True)
    telefono = models.CharField('Telefono', max_length=20, blank=True, null=True)
    email = models.EmailField('Correo Electronico', blank=True, null=True)
    web = models.URLField('Web', blank=True, null=True)
    #xpos VARCHAR(21)
    #ypos VARCHAR(21)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class Fotografia_contenido(models.Model):
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE, related_name='fotografias')
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = HTMLField(blank=True, null=True)
    imagen = models.FileField(upload_to='fotografias')
    def __str__(self):
        return self.nombre
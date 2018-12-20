#Importamos modulos standars
import datetime
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Provincia(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    mod_time = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    def as_dict(self):
        return {
            "id_provincia": self.id,
            "nombre": self.nombre,
            "mod_time": self.mod_time,
        }

class Localidad(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='localidades')
    nombre = models.CharField(max_length=150, unique=True)
    #xpos VARCHAR(21)
    #ypos VARCHAR(21)
    mod_time = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    def as_dict(self):
        return {
            "id_provincia": self.provincia.id,
            "id_localidad": self.id,
            "nombre": self.nombre,
            "mod_time": self.mod_time,
        }

class Fotografia_localidad(models.Model):
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name='fotografias')
    imagen = models.FileField(upload_to='fotografias')
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = HTMLField(blank=True, null=True)
    mod_time = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    def as_dict(self):
        return {
            "id_localidad": self.localidad.id,
            "id_fotografia": self.id,
            "nombre": self.nombre,
            "ruta": self.imagen.url,
            "descripcion": self.descripcion,
            "mod_time": self.mod_time,
        }

class Tipo_contenido(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    mod_time = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    def as_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "mod_time": self.mod_time,
        }

class Contenido(models.Model):
    localidad  = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name='contenidos')
    tipo_contenido  = models.ForeignKey(Tipo_contenido, on_delete=models.CASCADE, related_name='contenidos')
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = HTMLField(blank=True, null=True)
    direccion = models.CharField('Direccion', max_length=200, blank=True, null=True)
    telefono = models.CharField('Telefono', max_length=20, blank=True, null=True)
    email = models.EmailField('Correo Electronico', blank=True, null=True)
    web = models.URLField('Web', blank=True, null=True)
    mod_time = models.DateTimeField(auto_now=True)
    #xpos VARCHAR(21)
    #ypos VARCHAR(21)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    def as_dict(self):
        return {
            "id_localidad": self.localidad.id,
            "id_tipo_contenido": self.tipo_contenido.id,
            "id_contenido": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "email": self.email,
            "web": self.web,
            "mod_time": self.mod_time,
        }

class Fotografia_contenido(models.Model):
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE, related_name='fotografias')
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = HTMLField(blank=True, null=True)
    imagen = models.FileField(upload_to='fotografias')
    mod_time = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    def as_dict(self):
        return {
            "id_contenido": self.contenido.id,
            "id_fotografia": self.id,
            "nombre": self.nombre,
            "ruta": self.imagen.url,
            "descripcion": self.descripcion,
            "mod_time": self.mod_time,
        }
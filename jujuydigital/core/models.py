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
            "mod_time": str(self.mod_time),
            "activo": str(self.activo),
        }

class Localidad(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='localidades')
    nombre = models.CharField(max_length=150, unique=True)
    gpos_lat = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    gpos_long = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    mod_time = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    def as_dict(self):
        return {
            "id_provincia": self.provincia.id,
            "id_localidad": self.id,
            "nombre": self.nombre,
            "gpos_lat": str(self.gpos_lat),
            "gpos_long": str(self.gpos_long),
            "mod_time": str(self.mod_time),
            "activo": str(self.activo),
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
            "mod_time": str(self.mod_time),
            "activo": str(self.activo),
        }

class Tipo_render(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    mod_time = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    def as_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "mod_time": str(self.mod_time),
            "activo": str(self.activo),
        }

class Tipo_contenido(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    tipo_render = models.ForeignKey(Tipo_render, on_delete=models.CASCADE, related_name='tipo_contenidos')
    mod_time = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    def as_dict(self):
        return {
            "id": self.id,
            "id_tipo_render": self.tipo_render.id,
            "nombre": self.nombre,
            "mod_time": str(self.mod_time),
            "activo": str(self.activo),
        }

class Fotografia_tipo_contenido(models.Model):
    tipo_contenido  = models.ForeignKey(Tipo_contenido, on_delete=models.CASCADE, related_name='fotografias_tipos_contenidos')
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = HTMLField(blank=True, null=True)
    imagen = models.FileField(upload_to='fotografias')
    mod_time = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    def as_dict(self):
        return {
            "id_tipo_contenido": self.tipo_contenido.id,
            "id_fotografia": self.id,
            "nombre": self.nombre,
            "ruta": self.imagen.url,
            "descripcion": self.descripcion,
            "mod_time": str(self.mod_time),
            "activo": str(self.activo),
        }

class Subtipo_contenido(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    mod_time = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    def as_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "mod_time": str(self.mod_time),
            "activo": str(self.activo),
        }

class Contenido(models.Model):
    localidad  = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name='contenidos')
    tipo_contenido  = models.ForeignKey(Tipo_contenido, default=1, on_delete=models.CASCADE, related_name='contenidos')
    subtipo_contenido  = models.ForeignKey(Subtipo_contenido, default=1, on_delete=models.CASCADE, related_name='contenidos')
    estrellas = models.IntegerField(default=1, blank=True, null=True)
    nombre = models.CharField(max_length=150)
    descripcion = HTMLField(blank=True, null=True)
    direccion = models.CharField('Direccion', max_length=200, blank=True, null=True)
    telefono = models.CharField('Telefono', max_length=20, blank=True, null=True)
    email = models.EmailField('Correo Electronico', blank=True, null=True)
    web = models.URLField('Web', blank=True, null=True)
    gpos_lat = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    gpos_long = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    fecha_inicio = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)
    fecha_fin = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)
    mod_time = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return (self.nombre + ' de ' + self.localidad.nombre)
    def as_dict(self):
        return {
            "id_localidad": self.localidad.id,
            "id_tipo_contenido": self.tipo_contenido.id,
            "id_subtipo_contenido": self.subtipo_contenido.id,
            "id_contenido": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "estrellas": self.estrellas,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "email": self.email,
            "web": self.web,
            "gpos_lat": str(self.gpos_lat),
            "gpos_long": str(self.gpos_long),
            "fecha_inicio": str(self.fecha_inicio),
            "fecha_fin": str(self.fecha_fin),
            "mod_time": str(self.mod_time),
            "activo": str(self.activo),
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
            "mod_time": str(self.mod_time),
            "activo": str(self.activo),
        }
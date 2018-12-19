import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#Imports del proyecto
from .models import Provincia, Localidad, Tipo_contenido, Fotografia_localidad, Contenido, Fotografia_contenido

# Create your views here.
def ws_provincias(request, mod_date=None, mod_time=None):
    provincias = Provincia.objects.filter(activo=True)
    if mod_date is not None:
        provincias = provincias.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    provincias = [func.as_dict() for func in provincias]
    return HttpResponse(json.dumps({"registros": len(provincias),"provincias": provincias}), content_type='application/json')

def ws_localidades(request, mod_date=None, mod_time=None):
    localidades = Localidad.objects.filter(activo=True)
    if mod_date is not None:
        localidades = localidades.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    localidades = [func.as_dict() for func in localidades]
    return HttpResponse(json.dumps({"registros": len(localidades),"localidades": localidades}), content_type='application/json')

def ws_fotografias_localidades(request, mod_date=None, mod_time=None):
    fotografias_localidades = Fotografia_localidad.objects.filter(activo=True)
    if mod_date is not None:
        fotografias_localidades = fotografias_localidades.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    fotografias_localidades = [func.as_dict() for func in fotografias_localidades]
    return HttpResponse(json.dumps({"registros": len(fotografias_localidades),"fotografias_localidades": fotografias_localidades}), content_type='application/json')

def ws_tipo_contenidos(request, mod_date=None, mod_time=None):
    tipo_contenidos = Tipo_contenido.objects.filter(activo=True)
    if mod_date is not None:
        tipo_contenidos = tipo_contenidos.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    tipo_contenidos = [func.as_dict() for func in tipo_contenidos]
    return HttpResponse(json.dumps({"registros": len(tipo_contenidos),"tipo_contenidos": tipo_contenidos}), content_type='application/json')

def ws_contenidos(request, mod_date=None, mod_time=None):
    contenidos = Contenido.objects.filter(activo=True)
    if mod_date is not None:
        contenidos = contenidos.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    contenidos = [func.as_dict() for func in contenidos]
    return HttpResponse(json.dumps({"registros": len(contenidos),"contenidos": contenidos}), content_type='application/json')

def ws_fotografias_contenidos(request, mod_date=None, mod_time=None):
    fotografias_contenidos = Fotografia_contenido.objects.filter(activo=True)
    if mod_date is not None:
        fotografias_contenidos = fotografias_contenidos.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    fotografias_contenidos = [func.as_dict() for func in fotografias_contenidos]
    return HttpResponse(json.dumps({"registros": len(fotografias_contenidos),"fotografias_contenidos": fotografias_contenidos}), content_type='application/json')
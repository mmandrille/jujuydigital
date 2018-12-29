import json
import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#Imports del proyecto
from .models import Provincia, Localidad, Fotografia_localidad, Tipo_contenido, Fotografia_tipo_contenido, Contenido, Fotografia_contenido

# Create your views here.
def ws_provincias(request, mod_date=None, mod_time=None):
    provincias = Provincia.objects.all()
    if mod_date is not None:
        provincias = provincias.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    provincias = [func.as_dict() for func in provincias]
    return HttpResponse(json.dumps({"registros_ws": len(provincias), "registros_tabla": Provincia.objects.all().count() ,"provincias": provincias}), content_type='application/json')

def ws_localidades(request, mod_date=None, mod_time=None):
    localidades = Localidad.objects.all()
    if mod_date is not None:
        localidades = localidades.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    localidades = [func.as_dict() for func in localidades]
    return HttpResponse(json.dumps({"registros_ws": len(localidades), "registros_tabla": Localidad.objects.all().count(), "localidades": localidades}), content_type='application/json')

def ws_fotografias_localidades(request, mod_date=None, mod_time=None):
    fotografias_localidades = Fotografia_localidad.objects.all()
    if mod_date is not None:
        fotografias_localidades = fotografias_localidades.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    fotografias_localidades = [func.as_dict() for func in fotografias_localidades]
    return HttpResponse(json.dumps({"registros_ws": len(fotografias_localidades), "registros_tabla": Fotografia_localidad.objects.all().count(),"fotografias_localidades": fotografias_localidades}), content_type='application/json')

def ws_tipo_contenidos(request, mod_date=None, mod_time=None):
    tipo_contenidos = Tipo_contenido.objects.all()
    if mod_date is not None:
        tipo_contenidos = tipo_contenidos.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    tipo_contenidos = [func.as_dict() for func in tipo_contenidos]
    return HttpResponse(json.dumps({"registros_ws": len(tipo_contenidos), "registros_tabla": Tipo_contenido.objects.all().count(), "tipo_contenidos": tipo_contenidos}), content_type='application/json')

def ws_fotografias_tipo_contenidos(request, mod_date=None, mod_time=None):
    fotografias_tipo_contenidos = Fotografia_tipo_contenido.objects.all()
    if mod_date is not None:
        fotografias_tipo_contenidos = fotografias_tipo_contenidos.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    fotografias_tipo_contenidos = [func.as_dict() for func in fotografias_tipo_contenidos]
    return HttpResponse(json.dumps({"registros_ws": len(fotografias_tipo_contenidos), "registros_tabla": Fotografia_tipo_contenido.objects.all().count(), "fotografias_tipo_contenidos": fotografias_tipo_contenidos}), content_type='application/json')

def ws_contenidos(request, mod_date=None, mod_time=None):
    contenidos = Contenido.objects.all()
    if mod_date is not None:
        contenidos = contenidos.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    contenidos = [func.as_dict() for func in contenidos]
    return HttpResponse(json.dumps({"registros_ws": len(contenidos), "registros_tabla": Contenido.objects.all().count(), "contenidos": contenidos}), content_type='application/json')

def ws_fotografias_contenidos(request, mod_date=None, mod_time=None):
    fotografias_contenidos = Fotografia_contenido.objects.all()
    if mod_date is not None:
        fotografias_contenidos = fotografias_contenidos.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    fotografias_contenidos = [func.as_dict() for func in fotografias_contenidos]
    return HttpResponse(json.dumps({"registros_ws": len(fotografias_contenidos), "registros_tabla": Fotografia_contenido.objects.all().count(), "fotografias_contenidos": fotografias_contenidos}), content_type='application/json')
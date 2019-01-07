import json
import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#decoradores
from django.contrib.admin.views.decorators import staff_member_required

#Imports del proyecto
import core.urls
from .models import Provincia, Localidad, Fotografia_localidad, Tipo_contenido, Subtipo_contenido, Tipo_render, Fotografia_tipo_contenido, Contenido, Fotografia_contenido

# Create your views here.
def home(request):
    dict_url = dict()
    for url in core.urls.urlpatterns:
        dict_url[url.lookup_str] = "/" + str(url.pattern).replace("$","")
    return render(request, 'home.html', {"dict_url": dict_url,})

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

def ws_subtipo_contenidos(request, mod_date=None, mod_time=None):
    subtipo_contenidos = Subtipo_contenido.objects.all()
    if mod_date is not None:
        subtipo_contenidos = subtipo_contenidos.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    subtipo_contenidos = [func.as_dict() for func in subtipo_contenidos]
    return HttpResponse(json.dumps({"registros_ws": len(subtipo_contenidos), "registros_tabla": Subtipo_contenido.objects.all().count(), "tipo_contenidos": subtipo_contenidos}), content_type='application/json')

def ws_tipo_render(request, mod_date=None, mod_time=None):
    tipo_render = Tipo_render.objects.all()
    if mod_date is not None:
        tipo_render = tipo_render.filter(mod_time__date__gte = mod_date, mod_time__time__gte = mod_time)
    tipo_render = [func.as_dict() for func in tipo_render]
    return HttpResponse(json.dumps({"registros_ws": len(tipo_render), "registros_tabla": Tipo_render.objects.all().count(), "tipo_render": tipo_render}), content_type='application/json')

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

@staff_member_required
def upload_csv_contenidos(request):
    data = {}
    if "GET" == request.method:
        return render(request, "upload_csv.html", data)
    # if not GET, then proceed
    csv_file = request.FILES["csv_file"]
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'File is not CSV type')
        return HttpResponseRedirect(reverse("core:upload_csv_contenidos"))
        #if file is too large, return
    if csv_file.multiple_chunks():
        messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
        return HttpResponseRedirect(reverse("core:upload_csv_contenidos"))
        
    file_data = csv_file.read().decode("utf-8")
    lines = file_data.split("\n")
    #loop over the lines and save them in db. If error , store as string and then display
    #llamar funcion cada 100 mails.
    count = 0
    for line in lines:
        if line:
            sline = line.split(";")
            contenido = Contenido()
            #Provincia
            if sline[0]:
                try: provincia = Provincia.objects.get(nombre=sline[0])
                except Provincia.DoesNotExist:
                    provincia = Provincia()
                    provincia.nombre = sline[0]
                    provincia.save()
                contenido.provincia = provincia
            #Localidad
            if sline[1]:
                try: localidad = Localidad.objects.get(nombre=sline[1])
                except Localidad.DoesNotExist:
                    localidad = Localidad()
                    localidad.provincia = contenido.provincia
                    localidad.nombre = sline[1]
                    localidad.save()
                contenido.localidad = localidad
            #Tipo Contenido
            if sline[2]:
                try: tipo_contenido = Tipo_contenido.objects.get(nombre=sline[2])
                except Tipo_contenido.DoesNotExist:
                    tipo_contenido = Tipo_contenido()
                    tipo_contenido.nombre = sline[2]
                    tipo_contenido.save()
                contenido.tipo_contenido = tipo_contenido
            #Tipo Contenido
            if sline[3]:
                try: subtipo_contenido = Subtipo_contenido.objects.get(nombre=sline[3])
                except Subtipo_contenido.DoesNotExist:
                    subtipo_contenido = Subtipo_contenido()
                    subtipo_contenido.nombre = sline[3]
                    subtipo_contenido.save()
                contenido.subtipo_contenido = subtipo_contenido
            #Tipo Render
            if sline[4]:
                try: tipo_render = Tipo_render.objects.get(nombre=sline[4])
                except Tipo_render.DoesNotExist:
                    tipo_render = Tipo_render()
                    tipo_render.nombre = sline[4]
                    tipo_render.save()
                contenido.tipo_render = tipo_render
            #Estrellas
            if sline[5]:
                contenido.estrellas = sline[5]
            #Nombre
            if sline[6]:
                contenido.nombre = sline[6]
            #Direccion
            if sline[7]:
                contenido.direccion = sline[7]            
            #Web
            if sline[8]:
                contenido.web = sline[8]            
            #Correo
            if sline[9]:
                contenido.email = sline[9]
            #Telefono
            if sline[10]:
                contenido.telefono = sline[10]            
            #Descripcion
            if sline[11]:
                contenido.descripcion = sline[11]
            #Fecha de Inicio
            if sline[12]:
                contenido.fecha_inicio = sline[12]
            #Fecha de Fin
            if sline[13]:
                contenido.fecha_fin = sline[13]
            #Una vez preparado, si aun no existe, lo creamos.
            try: 
                contenido =  Contenido.objects.get(nombre=contenido.nombre, localidad=contenido.localidad)
            except Contenido.DoesNotExist:
                contenido.save()
    return render(request, 'upload_csv.html', {'count': len(lines)})
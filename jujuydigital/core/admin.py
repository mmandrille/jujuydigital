from django.contrib import admin

#Incluimos modelos
from .models import Provincia, Localidad, Fotografia_localidad, Tipo_contenido, Contenido, Fotografia_contenido

#Definimos inlines
#Localidad
class FotoLocalidad(admin.TabularInline):
    model = Fotografia_localidad

class LocalidadAdmin(admin.ModelAdmin):
    inlines = [
        FotoLocalidad,
    ]

#Contenidos
class FotoContenido(admin.TabularInline):
    model = Fotografia_contenido

class ContenidoAdmin(admin.ModelAdmin):
    inlines = [
        FotoContenido,
    ]

# Register your models here.
admin.site.register(Provincia)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Tipo_contenido)
admin.site.register(Contenido, ContenidoAdmin)
from django.contrib import admin

#Incluimos modelos
from .models import Provincia, Localidad, Fotografia_localidad, Tipo_contenido, Subtipo_contenido, Fotografia_tipo_contenido, Tipo_render, Contenido, Fotografia_contenido

#Definimos inlines
#Localidad
class FotoLocalidad(admin.TabularInline):
    model = Fotografia_localidad

class LocalidadAdmin(admin.ModelAdmin):
    inlines = [
        FotoLocalidad,
    ]

#Tipo_Contenidos
class FotoTipoContenido(admin.TabularInline):
    model = Fotografia_tipo_contenido

class TipoContenidoAdmin(admin.ModelAdmin):
    inlines = [
        FotoTipoContenido,
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
admin.site.register(Tipo_contenido, TipoContenidoAdmin)
admin.site.register(Subtipo_contenido)
admin.site.register(Tipo_render)
admin.site.register(Contenido, ContenidoAdmin)
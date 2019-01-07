from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    #Web Services
    url(r'^$', views.home, name='home'),

    url(r'ws/provincias/(?P<mod_date>\d{4}-\d{2}-\d{2})-(?P<mod_time>\d{2}:\d{2})/$', views.ws_provincias, name='ws_provincias'),
    url(r'ws/provincias/$', views.ws_provincias, name='ws_provincias'),

    url(r'ws/localidades/(?P<mod_date>\d{4}-\d{2}-\d{2})-(?P<mod_time>\d{2}:\d{2})/$', views.ws_localidades, name='ws_localidades'),
    url(r'ws/localidades/$', views.ws_localidades, name='ws_localidades'),

    url(r'ws/fotografias_localidades/(?P<mod_date>\d{4}-\d{2}-\d{2})-(?P<mod_time>\d{2}:\d{2})/$', views.ws_fotografias_localidades, name='ws_fotografias_localidades'),
    url(r'ws/fotografias_localidades/$', views.ws_fotografias_localidades, name='ws_fotografias_localidades'),
    
    url(r'ws/tipo_contenidos/(?P<mod_date>\d{4}-\d{2}-\d{2})-(?P<mod_time>\d{2}:\d{2})/$', views.ws_tipo_contenidos, name='ws_tipo_contenidos'),
    url(r'ws/tipo_contenidos/$', views.ws_tipo_contenidos, name='ws_tipo_contenidos'),

    url(r'ws/subtipo_contenidos/(?P<mod_date>\d{4}-\d{2}-\d{2})-(?P<mod_time>\d{2}:\d{2})/$', views.ws_subtipo_contenidos, name='ws_subtipo_contenidos'),
    url(r'ws/subtipo_contenidos/$', views.ws_subtipo_contenidos, name='ws_subtipo_contenidos'),

    url(r'ws/tipo_render/(?P<mod_date>\d{4}-\d{2}-\d{2})-(?P<mod_time>\d{2}:\d{2})/$', views.ws_tipo_render, name='ws_tipo_render'),
    url(r'ws/tipo_render/$', views.ws_tipo_render, name='ws_tipo_render'),

    url(r'ws/fotografias_tipo_contenidos/(?P<mod_date>\d{4}-\d{2}-\d{2})-(?P<mod_time>\d{2}:\d{2})/$', views.ws_fotografias_tipo_contenidos, name='ws_fotografias_tipo_contenidos'),
    url(r'ws/fotografias_tipo_contenidos/$', views.ws_fotografias_tipo_contenidos, name='ws_fotografias_tipo_contenidos'),

    url(r'ws/contenidos/(?P<mod_date>\d{4}-\d{2}-\d{2})-(?P<mod_time>\d{2}:\d{2})/$', views.ws_contenidos, name='ws_contenidos'),
    url(r'ws/contenidos/$', views.ws_contenidos, name='ws_contenidos'),
    
    url(r'ws/fotografias_contenidos/(?P<mod_date>\d{4}-\d{2}-\d{2})-(?P<mod_time>\d{2}:\d{2})/$', views.ws_fotografias_contenidos, name='ws_fotografias_contenidos'),
    url(r'ws/fotografias_contenidos/$', views.ws_fotografias_contenidos, name='ws_fotografias_contenidos'),

    url(r'upload/csv/contenidos$', views.upload_csv_contenidos, name='upload_csv_contenidos'),
]
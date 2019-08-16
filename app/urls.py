# Written By Ismael Heredia in the year 2018

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from app.views import home,wallpapers,importar,exportar

urlpatterns = [

    url(r'^$', wallpapers.manager_wallpaper_list, name='inicio'),
    url(r'^wallpapers/$',  wallpapers.manager_wallpaper_list, name='manager_wallpaper_list'),
    url(r'^wallpapers/agregar$', wallpapers.manager_wallpaper_view, name='manager_wallpaper_view'),
    url(r'^wallpapers/editar/(?P<id_wallpaper>\d+)/$', wallpapers.manager_wallpaper_edit, name='manager_wallpaper_edit'),
    url(r'^wallpapers/borrar/(?P<id_wallpaper>\d+)/$', wallpapers.manager_wallpaper_delete, name='manager_wallpaper_delete'),
    url(r'^importar/$',  importar.manager_importar_form, name='manager_importar_form'),
    url(r'^exportar/$',  exportar.manager_exportar_form, name='manager_exportar_form'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
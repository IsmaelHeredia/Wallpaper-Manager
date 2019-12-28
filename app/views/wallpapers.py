# Written By Ismael Heredia in the year 2018

import os
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Wallpaper
from app.services import Service
from app.functions import Function
from app.forms import WallpaperForm
from django.conf import settings

def manager_wallpaper_list(request):
    wallpapers = Wallpaper.objects.all().order_by('fecha_registro')
    return render(request, 'wallpapers/wallpaper_list.html', {'wallpapers':wallpapers})

def manager_wallpaper_view(request):
    if request.method == 'POST':
        form = WallpaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message_text = "El wallpaper fue registrado"
            messages.add_message(request, messages.SUCCESS,message_text)
            return redirect("manager_wallpaper_list")
        else:
            message_text = "Faltan datos para registrar el wallpaper"
            messages.add_message(request, messages.WARNING,message_text)
            return redirect("manager_wallpaper_view")
    else:
        return render(request, 'wallpapers/wallpaper_form.html', {'form':WallpaperForm(),'nuevo':True})

def manager_wallpaper_edit(request,id_wallpaper):
    wallpaper = get_object_or_404(Wallpaper, id=id_wallpaper)
    if request.method == 'GET':
        form = WallpaperForm(instance=wallpaper)
    else:
        form = WallpaperForm(request.POST,instance=wallpaper)
        if form.is_valid():
            form.save()
            message_text = "El wallpaper fue actualizado"
            messages.add_message(request, messages.SUCCESS,message_text)
            return redirect("manager_wallpaper_list")                 
        else:
            message_text = "Faltan datos para actualizar el wallpaper"
            messages.add_message(request, messages.WARNING,message_text)  
            return redirect("manager_wallpaper_edit",id_wallpaper)    
    return render(request,'wallpapers/wallpaper_form.html',{'form':form,'wallpaper':wallpaper})

def manager_wallpaper_delete(request,id_wallpaper):
    wallpaper = get_object_or_404(Wallpaper, id=id_wallpaper)
    if request.method == 'POST':
        if 'borrar_wallpaper' in request.POST:
            fullpath = wallpaper.imagen.path
            os.remove(fullpath)
            wallpaper.delete()
            message_text = "El wallpaper fue borrado definitivamente"
            messages.add_message(request, messages.SUCCESS,message_text)
            return redirect('manager_wallpaper_list')
        elif 'volver_lista' in request.POST:
            return redirect('manager_wallpaper_list')    
    return render(request,'wallpapers/wallpaper_delete.html',{'wallpaper':wallpaper})
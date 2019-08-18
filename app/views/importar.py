# Written By Ismael Heredia in the year 2018

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import View
from django.contrib import messages
from app.services import Service
from app.functions import Function
from app.forms import ImportarForm

service = Service()
function = Function()

def manager_importar_form(request):
    if request.method == 'POST':
        form = ImportarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            directorio = data['directorio']
            message_text = ""
            if service.importar_datos(directorio):
                message_text = "Los datos fueron importados exitosamente"
                messages.add_message(request, messages.SUCCESS,message_text)
                return redirect("manager_wallpaper_list")
            else:
                message_text = "Ha ocurrido un error en la importación"
                messages.add_message(request, messages.WARNING,message_text)
                return render(request, 'importar/index.html', {'form':ImportarForm()})
    else:
        return render(request, 'importar/index.html', {'form':ImportarForm()})
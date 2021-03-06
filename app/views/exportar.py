# Written By Ismael Heredia in the year 2018

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import View
from django.contrib import messages
from app.services import Service
from app.functions import Function
from app.forms import ExportarForm

service = Service()
function = Function()

def manager_exportar_form(request):
    if request.method == 'POST':
        form = ExportarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            directorio = data['directorio']
            message_text = ""
            if service.exportar_datos(directorio):
                message_text = "Los datos exportados exitosamente"
                messages.add_message(request, messages.SUCCESS,message_text)
                return redirect("manager_wallpaper_view")
            else:
                message_text = "Ha ocurrido un error en la exportación"
                messages.add_message(request, messages.WARNING,message_text)
                return render(request, 'exportar/index.html', {'form':ExportarForm()})
    else:
        return render(request, 'exportar/index.html', {'form':ExportarForm()})
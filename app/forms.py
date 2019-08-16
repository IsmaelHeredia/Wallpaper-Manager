# Written By Ismael Heredia in the year 2017

from django import forms

from app.models import Wallpaper,Importar,Exportar

class WallpaperForm(forms.ModelForm):

    imagen = forms.FileField()
    verano = forms.BooleanField(required=False, initial=False)
    otoño = forms.BooleanField(required=False, initial=False)
    invierno = forms.BooleanField(required=False, initial=False)
    primavera = forms.BooleanField(required=False, initial=False)
    amanecer = forms.BooleanField(required=False, initial=False)
    mañana = forms.BooleanField(required=False, initial=False)
    tarde = forms.BooleanField(required=False, initial=False)
    noche = forms.BooleanField(required=False, initial=False)

    class Meta:
        
        model = Wallpaper

        fields = [
            'imagen',
            'verano',
            'otoño',
            'invierno',
            'primavera',
            'amanecer',
            'mañana',
            'tarde',
            'noche',
        ]

        labels = {
            'imagen':'Imagen',
            'verano':'Verano',
            'otoño':'Otoño',
            'invierno':'Invierno',
            'primavera':'Primavera',
            'amanecer':'Amanecer',
            'mañana':'Mañana',
            'tarde':'Tarde',
            'noche':'Noche',
        }

class ImportarForm(forms.ModelForm):
    
    class Meta:

        model = Importar
        
        fields=[
            'directorio',
        ]
        
        labels = {
            'directorio' : 'Directorio',
        }

        widgets = {
            'directorio' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese directorio','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
        }

class ExportarForm(forms.ModelForm):
    
    class Meta:

        model = Exportar
        
        fields=[
            'directorio',
        ]
        
        labels = {
            'directorio' : 'Directorio',
        }

        widgets = {
            'directorio' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese directorio','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
        }
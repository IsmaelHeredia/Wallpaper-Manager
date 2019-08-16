import os,time,datetime,re,ntpath,shutil
from app.functions import Function
from app.models import Wallpaper
from django.core.files import File
from django.conf import settings

function = Function()

class Service(object):

    def importar_datos(self,directorio):

        respuesta = False

        try:
            if os.path.exists(directorio):
                
                print("Importando datos ...\n")

                print("\nListando wallpapers en %s ...\n" % (directorio,))

                if os.path.isdir(directorio):
                    wallpapers = os.listdir(directorio)
                    print(len(wallpapers))
                    for wallpaper in wallpapers:
                        wallpaper_ruta = directorio + "\\" + wallpaper
                        print(wallpaper_ruta)
                        if os.path.isfile(wallpaper_ruta):
                            print("\nWallpaper : "+wallpaper)

                            wallpaper_nombre = os.path.basename(wallpaper_ruta)

                            verano = False
                            otoño = False
                            invierno = False
                            primavera = False
                            amanecer = False
                            mañana = False
                            tarde = False
                            noche = False

                            dividir_nombre = wallpaper_nombre.split("_")
                            nombre = dividir_nombre[0]
                            estaciones = dividir_nombre[1]
                            momentos = dividir_nombre[2]

                            nuevo_nombre = nombre + ".jpg"

                            if "v" in estaciones:
                              verano = True
                            if "o" in estaciones:
                              otoño = True
                            if "i" in estaciones:
                              invierno = True
                            if "p" in estaciones:
                              primavera = True

                            if "a" in momentos:
                              amanecer = True
                            if "m" in momentos:
                              mañana = True
                            if "t" in momentos:
                              tarde = True
                            if "n" in momentos:
                              noche = True

                            reopen = open(wallpaper_ruta, "rb")
                            wallpaper_archivo = File(reopen)

                            wallpaper_object = Wallpaper()
                            wallpaper_object.imagen.save(nuevo_nombre, wallpaper_archivo, save=True)
                            wallpaper_object.verano = verano
                            wallpaper_object.otoño = otoño
                            wallpaper_object.invierno = invierno
                            wallpaper_object.primavera = primavera
                            wallpaper_object.amanecer = amanecer
                            wallpaper_object.mañana = mañana
                            wallpaper_object.tarde = tarde
                            wallpaper_object.noche = noche
                            wallpaper_object.save()

                else:
                    print("No se encontraron wallpapers")

                respuesta = True

        except:
            raise

        return respuesta

    def exportar_datos(self,directorio):

        respuesta = False

        try:
            if os.path.exists(directorio):   

                wallpapers = Wallpaper.objects.all().order_by('fecha_registro')
                for wallpaper in wallpapers:
                    wallpaper_ruta = wallpaper.imagen.path
                    print("Wallpaper ruta %s" % (wallpaper_ruta,))

                    verano = wallpaper.verano
                    otoño = wallpaper.otoño
                    invierno = wallpaper.invierno
                    primavera = wallpaper.primavera
                    amanecer = wallpaper.amanecer
                    mañana = wallpaper.mañana
                    tarde = wallpaper.tarde
                    noche = wallpaper.noche

                    estaciones = ""
                    momentos = ""

                    if verano:
                      estaciones = estaciones + "v"
                    if otoño:
                      estaciones = estaciones + "o"
                    if invierno:
                      estaciones = estaciones + "i"
                    if primavera:
                      estaciones = estaciones + "p"       

                    if amanecer:
                      momentos = momentos + "a"   
                    if mañana:
                      momentos = momentos + "m"   
                    if tarde:
                      momentos = momentos + "t"   
                    if noche:
                      momentos = momentos + "n"   

                    nuevo_nombre = os.path.splitext(ntpath.basename(wallpaper_ruta))[0] + "_" + estaciones + "_" + momentos + ".jpg"
                    wallpaper_copiado = directorio + "\\" + nuevo_nombre
                    print("Wallpaper copiado %s" % (wallpaper_copiado,))

                    if os.path.exists(wallpaper_ruta):
                      shutil.copy2(wallpaper_ruta,wallpaper_copiado)
                      
                print("Datos exportados")

                respuesta = True

        except:
            raise

        return respuesta

    def destroy(self):
        pass
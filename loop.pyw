#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3,os,datetime,time,random,keyboard
from time import gmtime, strftime, sleep
from datetime import date, datetime
import threading
import os,os.path,re,ctypes

SPI_SETDESKWALLPAPER = 20

db_name = "db.sqlite3"

Y = 2000

estaciones = [('Verano', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('Otoño', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('Invierno', (date(Y,  6, 21),  date(Y,  9, 20))),
           ('Primavera', (date(Y,  9, 21),  date(Y, 12, 20))),
           ('Verano', (date(Y, 12, 21),  date(Y, 12, 31)))]

class Wallpaper:
  id = ""
  imagen = ""
  verano = ""
  otoño = ""
  invierno = ""
  primavera = ""
  amanecer = ""
  mañana = ""
  tarde = ""
  noche = ""
  fecha_registro = ""
  def __init__(self,id_wallpaper,imagen,verano,otoño,invierno,primavera,amanecer,mañana,tarde,noche,fecha_registro):
    self.id = id_wallpaper
    self.imagen = imagen
    self.verano = verano
    self.otoño = otoño
    self.invierno = invierno
    self.primavera = primavera
    self.amanecer = amanecer
    self.mañana = mañana
    self.tarde = tarde
    self.noche = noche
    self.fecha_registro = fecha_registro

def listarWallpapers(epoca,momento):
  wallpapers_list = []
  con_bd = sqlite3.connect(db_name)
  cursor = con_bd.cursor()

  sql = "SELECT id,imagen,verano,otoño,invierno,primavera,amanecer,mañana,tarde,noche,fecha_registro FROM app_wallpaper"

  if epoca == "Verano":
    sql = sql + " WHERE verano"
  elif epoca == "Otoño":
    sql = sql + " WHERE otoño"
  elif epoca == "Invierno":
    sql = sql + " WHERE invierno"
  elif epoca == "Primavera":
    sql = sql + " WHERE primavera"

  if momento == "Amanecer":
    sql = sql + " AND amanecer"
  elif momento == "Mañana":
    sql = sql + " AND mañana"
  elif momento == "Tarde":
    sql = sql + " AND tarde"
  elif momento == "Noche":
    sql = sql + " AND noche"

  print(sql)

  cursor.execute(sql)

  wallpapers = cursor.fetchall()
  
  for wallpaper in wallpapers:
    id_wallpaper = wallpaper[0]
    imagen = wallpaper[1]
    verano = wallpaper[2]
    otoño = wallpaper[3]
    invierno = wallpaper[4]
    primavera = wallpaper[5]
    amanecer = wallpaper[6]
    mañana = wallpaper[7]
    tarde = wallpaper[8]
    noche = wallpaper[9]
    fecha_registro = wallpaper[10]
    
    wallpaper_obj = Wallpaper(id_wallpaper,imagen,verano,otoño,invierno,primavera,amanecer,mañana,tarde,noche,fecha_registro)
    wallpapers_list.append(wallpaper_obj)

  cursor.close()
  con_bd.commit()
  con_bd.close()
  return wallpapers_list

def reconocer_estacion(ahora):
    if isinstance(ahora, datetime):
        ahora = ahora.date()
    ahora = ahora.replace(year=Y)
    return next(estacion for estacion, (desde, hasta) in estaciones
                if desde <= ahora <= hasta)

def reconocerTiempo():

  dates_specials = {"25-12":"Navidad","1-1":"Año nuevo","":"","":"","":"","":"","":"","":""}

  datetime = time.localtime(time.time())

  year = datetime.tm_year
  month = datetime.tm_mon
  day = datetime.tm_mday

  hour = datetime.tm_hour
  minutes = datetime.tm_min
  seconds = datetime.tm_sec

  date_full = str(day) + "/" + str(month) + "/" + str(year)
  hour_full = str(hour) + ":" + str(minutes) + ":" + str(seconds)

  print("Date : %s" % (date_full,))
  print("Hour : %s" % (hour_full,))

  verano = False
  otoño = False
  invierno = False
  primavera = False

  estacion = reconocer_estacion(date.today())

  if estacion == "Verano":
    verano = True
  elif estacion == "Otoño":
    otoño = True
  elif estacion == "Invierno":
    invierno = True
  elif estacion == "Primavera":
    primavera = True

  mañana = False
  tarde = False
  noche = False
  amanecer = False

  if hour >= 6 and hour <= 11:
    mañana = True

  if hour >= 12 and hour <= 18:
    tarde = True

  if hour >= 19 and hour <= 23:
    noche = True

  if hour >= 24 and hour <= 5:
    madrugada = True

  epoca = ""
  momento = ""

  if verano:
    epoca = "Verano"
  elif otoño:
    epoca = "Otoño"
  elif invierno:
    epoca = "Invierno"
  elif primavera:
    epoca = "Primavera"

  if mañana:
    momento = "Mañana"
  elif tarde:
    momento = "Tarde"
  elif noche:
    momento = "Noche"
  elif amanecer:
    momento = "Amanecer"

  return epoca, momento

def cambiarFondo():
  epoca, momento = reconocerTiempo()
  print("[+] Buscando wallpapers en la epoca %s y el tiempo %s\n" % (epoca,momento,))
  wallpapers = listarWallpapers(epoca,momento)
  print("[+] Se encontraron %d wallpapers con esos parametros\n" % (len(wallpapers),))
  wallpaper = random.choice(wallpapers)
  ruta = os.getcwd()+"/media/"+wallpaper.imagen
  print("[+] Cargando wallpaper en la ubicación %s\n" % (ruta,))
  id_wallpaper = wallpaper.id
  imagen = wallpaper.imagen
  verano = wallpaper.verano
  otoño = wallpaper.otoño
  invierno = wallpaper.invierno
  primavera = wallpaper.primavera
  amanecer = wallpaper.amanecer
  mañana = wallpaper.mañana
  tarde = wallpaper.tarde
  noche = wallpaper.noche
  fecha_registro = wallpaper.fecha_registro
  print("[+] ID : %s" % (id_wallpaper,))
  print("[+] Imagen : %s" % (imagen,))
  print("[+] Verano : %s" % (verano,))
  print("[+] Otoño : %s" % (otoño,))
  print("[+] Invierno : %s" % (invierno,))
  print("[+] Primavera : %s" % (primavera,))
  print("[+] Mañana : %s" % (mañana,))
  print("[+] Tarde : %s" % (tarde,))
  print("[+] Noche : %s" % (noche,))
  print("[+] Fecha registro : %s" % (fecha_registro,))
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, ruta , 0)
  print("\n[+] Wallpaper cambiado\n")

def loop():
  tiempo = 3600 # Segundos
  threading.Timer(tiempo, loop).start()
  cambiarFondo()

def main():
  loop()
  keyboard.add_hotkey('ctrl+shift+a', cambiarFondo)
  keyboard.wait()

if __name__ == '__main__':
  main()
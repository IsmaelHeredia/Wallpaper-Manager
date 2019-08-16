from django.db import models
import datetime

class Wallpaper(models.Model):
    imagen = models.FileField(upload_to='wallpapers/')
    verano = models.BooleanField(default=False)
    otoño = models.BooleanField(default=False)
    invierno = models.BooleanField(default=False)
    primavera = models.BooleanField(default=False)
    amanecer = models.BooleanField(default=False)
    mañana = models.BooleanField(default=False)
    tarde = models.BooleanField(default=False)
    noche = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.fecha_registro is None:
            self.fecha_registro = datetime.datetime.now()
        super(Wallpaper, self).save(*args, **kwargs)

    def nombre(self):
        partes = self.imagen.path.split("\\")
        nombre = partes[-1]
        return nombre

    def __str__(self):
        return self.imagen

class Importar(models.Model):
    directorio = models.CharField(max_length=300)

    class Meta:
        managed = False

    def __str__(self):
        return self.directorio

class Exportar(models.Model):
    directorio = models.CharField(max_length=300)

    class Meta:
        managed = False

    def __str__(self):
        return self.directorio


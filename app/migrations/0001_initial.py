# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-04-29 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exportar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directorio', models.CharField(max_length=300)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Importar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directorio', models.CharField(max_length=300)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wallpaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.FileField(upload_to='wallpapers/')),
                ('verano', models.BooleanField(default=False)),
                ('otoño', models.BooleanField(default=False)),
                ('invierno', models.BooleanField(default=False)),
                ('primavera', models.BooleanField(default=False)),
                ('amanecer', models.BooleanField(default=False)),
                ('mañana', models.BooleanField(default=False)),
                ('tarde', models.BooleanField(default=False)),
                ('noche', models.BooleanField(default=False)),
                ('fecha_registro', models.DateTimeField()),
            ],
        ),
    ]

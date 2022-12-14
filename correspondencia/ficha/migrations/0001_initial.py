# Generated by Django 3.2 on 2022-12-02 18:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True, verbose_name='Nombre')),
                ('siglas', models.CharField(max_length=20, unique=True, verbose_name='Siglas')),
            ],
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True, verbose_name='Nombre')),
                ('siglas', models.CharField(max_length=20, unique=True, verbose_name='Siglas')),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id_ficha', models.IntegerField(max_length=6, primary_key=True, serialize=False, verbose_name='No. de Ficha')),
                ('fecha', models.DateField(default=datetime.datetime.now, verbose_name='Fecha')),
                ('num_documento', models.CharField(max_length=200, verbose_name='Número del Documento')),
                ('fecha_documento', models.DateField(default=datetime.datetime.now, verbose_name='Fecha del Documento')),
                ('nombre_firma', models.CharField(max_length=350, verbose_name='Nombre de quien firma')),
                ('asunto', models.CharField(max_length=500, verbose_name='Asunto')),
                ('instruccion', models.TextField(max_length=800, verbose_name='Instrucción')),
                ('prioridad', models.CharField(choices=[('1', 'Alta'), ('2', 'Media'), ('3', 'Baja')], default='3', max_length=6, verbose_name='Prioridad de la ficha')),
                ('resolucion', models.TextField(default='Sin resolución', max_length=800, verbose_name='Resolución')),
                ('fecha_recibido', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de ficha firmada')),
                ('estatus', models.CharField(choices=[('1', 'Atendido'), ('2', 'Sin atender')], default='2', max_length=12)),
                ('pdf_dependencia', models.FileField(blank=True, null=True, upload_to='pdfs/', verbose_name='PDF de la dependencia')),
                ('area_turnada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.area', verbose_name='Area a la que se turna')),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.dependencia', verbose_name='Dependencia Procedente')),
            ],
        ),
    ]

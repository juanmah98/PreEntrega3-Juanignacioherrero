# Generated by Django 4.1.5 on 2023-02-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('mensaje', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_orden', models.IntegerField()),
                ('fecha_compra', models.DateTimeField()),
                ('telefono', models.IntegerField()),
                ('nombre_apellido', models.CharField(max_length=30)),
                ('prendas_motivo', models.TextField(max_length=400)),
                ('domicilio', models.CharField(max_length=40)),
            ],
        ),
    ]

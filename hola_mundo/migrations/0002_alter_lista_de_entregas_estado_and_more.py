# Generated by Django 4.2 on 2023-04-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hola_mundo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista_de_entregas',
            name='estado',
            field=models.CharField(default='Por Hacer', max_length=40),
        ),
        migrations.AlterField(
            model_name='lista_de_entregas',
            name='nombre_entrega',
            field=models.TextField(max_length=40),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='apellido',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nick_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.TextField(max_length=100),
        ),
    ]

# Generated by Django 4.1 on 2022-09-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppInicio", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="jugador",
            name="apellido",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="jugador",
            name="edad",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="jugador",
            name="equipo",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="jugador",
            name="pais",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="jugador",
            name="posicion",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="jugador",
            name="nombre",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

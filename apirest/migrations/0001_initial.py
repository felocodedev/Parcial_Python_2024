# Generated by Django 5.0.6 on 2024-06-12 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=10)),
                ('identificacion', models.CharField(max_length=15)),
                ('genero', models.PositiveSmallIntegerField()),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
    ]

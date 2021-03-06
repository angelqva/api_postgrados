# Generated by Django 3.2.9 on 2022-06-22 23:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudiantes', '0001_initial'),
        ('profesores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nacional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=150, unique=True)),
                ('tema', models.CharField(max_length=150)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('cantidad_horas', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('impartido_universidad', models.BooleanField(default=True)),
                ('estudiantes', models.ManyToManyField(related_name='estudiantes', to='estudiantes.Estudiante')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesores.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Internacional',
            fields=[
                ('nacional_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='postgrados.nacional')),
                ('pais_impartido', models.CharField(max_length=150)),
                ('primera_vez', models.BooleanField(default=True)),
            ],
            bases=('postgrados.nacional',),
        ),
    ]

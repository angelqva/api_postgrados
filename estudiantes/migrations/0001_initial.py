# Generated by Django 3.2.9 on 2022-06-22 23:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnet_identidad', models.CharField(max_length=11, unique=True)),
                ('nombre', models.CharField(max_length=150)),
                ('apellidos', models.CharField(max_length=150)),
                ('edad', models.IntegerField(validators=[django.core.validators.MinValueValidator(18)])),
                ('especialidad', models.CharField(max_length=150)),
                ('nacionalidad', models.CharField(help_text='país donde nació', max_length=150)),
                ('residencia', models.CharField(help_text='país donde vive', max_length=150)),
                ('graduacion', models.CharField(help_text='Año de Graduación yyyy', max_length=4, verbose_name=django.core.validators.RegexValidator('^[0-9]*$', 'Enter a valid year'))),
                ('sexo', models.CharField(help_text='Default Masculino', max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

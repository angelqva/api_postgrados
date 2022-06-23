from django.db import models
from django.core.validators import RegexValidator
from informacion_personal.models import InformacionPersonal

# Create your models here.


class Estudiante(InformacionPersonal):
    nacionalidad = models.CharField(
        max_length=150, help_text='país donde nació')
    residencia = models.CharField(max_length=150, help_text='país donde vive')
    graduacion = models.CharField(
        RegexValidator(
            r"^[0-9]*$", "Enter a valid year"
        ),
        max_length=4, help_text='Año de Graduación yyyy')
    sexo = models.CharField(max_length=150, help_text='Default Masculino')

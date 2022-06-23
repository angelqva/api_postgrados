from django.db import models
from informacion_personal.models import InformacionPersonal

# Create your models here.


class Profesor(InformacionPersonal):
    CIENTIFICA = (
        ('Ninguna', 'Ninguna'),
        ('Master', 'Master'),
        ('Doctor', 'Doctor')
    )
    DOCENTE = (
        ('Asistente', 'Asistente'),
        ('Ausiliar', 'Ausiliar'),
        ('Instructor', 'Instructor'),
        ('Titular', 'Titular')
    )
    categoria_cientifica = models.CharField(
        choices=CIENTIFICA,
        max_length=7, help_text='Valor por defecto Ninguna')
    categoria_docente = models.CharField(
        choices=DOCENTE,
        max_length=10, help_text='Valor por defecto Titular')

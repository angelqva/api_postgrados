from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class InformacionPersonal(models.Model):
    carnet_identidad = models.CharField(unique=True, max_length=11)
    nombre = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    edad = models.IntegerField(validators=[MinValueValidator(18)])
    especialidad = models.CharField(max_length=150)

    class Meta:
        abstract = True

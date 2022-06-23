from django.db import models
from estudiantes.models import Estudiante
from profesores.models import Profesor
from django.core.validators import MinValueValidator


class Nacional(models.Model):
    codigo = models.CharField(unique=True, max_length=150)
    tema = models.CharField(max_length=150)
    inicio = models.DateField()
    fin = models.DateField()
    cantidad_horas = models.IntegerField(validators=[MinValueValidator(1)])
    impartido_universidad = models.BooleanField(default=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(
        Estudiante, related_name='estudiantes')

    def __str__(self):
        return f'Postgrado Nacional:{self.codigo}-{self.tema}'


class Internacional(Nacional):
    pais_impartido = models.CharField(max_length=150)
    primera_vez = models.BooleanField(default=True)

    def __str__(self):
        return f'Postgrado Internacional:{self.codigo}-{self.tema}'

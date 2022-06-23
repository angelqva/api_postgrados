from rest_framework import serializers
from estudiantes.models import Estudiante
from typing import *


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

from rest_framework import serializers
from postgrados.models import Nacional, Internacional
from profesores.serializers import Profesor, ProfesorSerializer
from estudiantes.serializers import Estudiante, EstudianteSerializer
from typing import *


class NacionalSerializer(serializers.ModelSerializer):
    profesor = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Profesor.objects.all(
    ), help_text='Primary key of Profesor')
    estudiantes = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Estudiante.objects.all(
    ), many=True, help_text='List of Primary keys of Estudiantes')

    class Meta:
        model = Nacional
        fields = '__all__'


class NacionalRead(serializers.ModelSerializer):
    profesor = ProfesorSerializer()
    estudiantes = EstudianteSerializer(many=True)

    class Meta:
        model = Nacional
        fields = '__all__'


class InternacionalSerializer(serializers.ModelSerializer):
    profesor = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Profesor.objects.all(
    ), help_text='Primary key of Profesor')
    estudiantes = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Estudiante.objects.all(
    ), many=True, help_text='List of Primary keys of Estudiantes')

    class Meta:
        model = Internacional
        fields = '__all__'


class InternacionalRead(serializers.ModelSerializer):
    profesor = ProfesorSerializer()
    estudiantes = EstudianteSerializer(many=True)

    class Meta:
        model = Internacional
        fields = '__all__'

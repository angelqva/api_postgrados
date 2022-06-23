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
    colegiatura = serializers.SerializerMethodField()

    class Meta:
        model = Nacional
        fields = ('id', 'codigo', 'tema', 'inicio', 'fin', 'cantidad_horas',
                  'impartido_universidad', 'profesor', 'estudiantes', 'colegiatura')

    def get_colegiatura(self, instance):
        obj: Nacional = instance
        credito = float(obj.cantidad_horas)/12
        nacional = 10*credito
        if obj.impartido_universidad is False:
            nacional += 15
        if obj.profesor.categoria_cientifica == 'doctor':
            nacional += 17
        if obj.profesor.categoria_cientifica == 'doctor':
            nacional += 9
        return round(nacional, 2)


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
    colegiatura = serializers.SerializerMethodField()

    class Meta:
        model = Internacional
        fields = ('id', 'codigo', 'tema', 'inicio', 'fin', 'cantidad_horas',
                  'impartido_universidad', 'profesor', 'estudiantes', 'colegiatura')

    def get_colegiatura(self, instance):
        obj: Internacional = instance
        credito = float(obj.cantidad_horas)/12
        internacional = 10*credito
        if obj.impartido_universidad is False:
            internacional += 15
        if obj.profesor.categoria_cientifica == 'doctor':
            internacional += 17
        if obj.profesor.categoria_cientifica == 'doctor':
            internacional += 9
        if obj.primera_vez:
            internacional += 20
        if obj.pais_impartido != 'Cuba':
            internacional += 50

        return round(internacional, 2)

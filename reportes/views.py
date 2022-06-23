from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from profesores.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
from postgrados.serializers import Nacional, Internacional
from typing import List
from datetime import datetime
from reportes.serializers import *


class ReporteView(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=["POST"], serializer_class=EspecialidadSerializer)
    def inciso_d(self, request, **kwargs):
        serializer = EspecialidadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        especialidad = request.data["especialidad"]
        postgrados_internacionales: List[Internacional] = list(
            Internacional.objects.filter(profesor__especialidad=especialidad, inicio__year=datetime.now().year).all())
        pi_menor_credito: Internacional = None
        for internacional in postgrados_internacionales:
            creditos = internacional.cantidad_horas/12
            if pi_menor_credito is None:
                pi_menor_credito = internacional
            else:
                creditos_menor = pi_menor_credito.cantidad_horas/12
                if creditos < creditos_menor:
                    pi_menor_credito = internacional
        if pi_menor_credito is not None:
            profesor_serializer = ProfesorSerializer(pi_menor_credito.profesor)
            return Response(data=profesor_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'No se encontraron postgrados internacionales con esa especialidad'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["POST"], serializer_class=CodigoSerializer)
    def inciso_b(self, request, **kwargs):
        serializer = CodigoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        codigo = request.data["codigo"]
        encontrado = False
        colegiatura = float(0.0)

        postgrado_nacional = Nacional.objects.filter(
            codigo=codigo, internacional__isnull=True)
        if postgrado_nacional.exists():
            encontrado = True
            obj: Nacional = postgrado_nacional.first()
            credito = float(obj.cantidad_horas)/12
            nacional = 10*credito
            if obj.impartido_universidad is False:
                nacional += 15
            if obj.profesor.categoria_cientifica == 'doctor':
                nacional += 17
            if obj.profesor.categoria_cientifica == 'doctor':
                nacional += 9
            colegiatura = round(nacional, 2)
        else:
            postgrado_internacional = Internacional.objects.filter(
                codigo=codigo)
            if postgrado_internacional.exists():
                encontrado = True
                obj: Internacional = postgrado_internacional.first()
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
                colegiatura = round(internacional, 2)
        if encontrado:
            return Response(data={'colegiatura': colegiatura}, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'No se encontro un postgrado con ese codigo'}, status=status.HTTP_200_OK)

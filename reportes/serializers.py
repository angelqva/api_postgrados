from rest_framework import serializers
from typing import *


class EspecialidadSerializer(serializers.Serializer):
    especialidad = serializers.CharField(required=True, allow_blank=False)


class CodigoSerializer(serializers.Serializer):
    codigo = serializers.CharField(required=True, allow_blank=False)

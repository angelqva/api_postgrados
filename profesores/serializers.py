from rest_framework import serializers
from profesores.models import Profesor
from typing import *


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

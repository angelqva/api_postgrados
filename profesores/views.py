from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from profesores.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
from postgrados.serializers import Internacional
from typing import List
from datetime import datetime


class ProfesorView(viewsets.ModelViewSet):
    serializer_class = ProfesorSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Profesor.objects.all()

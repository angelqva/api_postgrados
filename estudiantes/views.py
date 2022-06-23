from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from estudiantes.serializers import *


class EstudianteView(viewsets.ModelViewSet):
    serializer_class = EstudianteSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Estudiante.objects.all()

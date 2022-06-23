from rest_framework import status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from users.serializers import *
from rest_framework_simplejwt.tokens import TokenError


class LogoutView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        success = True
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except TokenError:
            success = False

        return Response({'success': success}, status=status.HTTP_200_OK)


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

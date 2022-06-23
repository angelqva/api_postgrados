from rest_framework.permissions import IsAuthenticated
from postgrados.serializers import *
from api.views import NestedSerializerMixin


class NacionalView(NestedSerializerMixin):
    serializer_class = NacionalSerializer
    read_serializer_class = NacionalRead
    permission_classes = (IsAuthenticated,)
    queryset = Nacional.objects.filter(internacional__isnull=True)


class InternacionalView(NestedSerializerMixin):
    serializer_class = InternacionalSerializer
    read_serializer_class = InternacionalRead
    permission_classes = (IsAuthenticated,)
    queryset = Internacional.objects.all()

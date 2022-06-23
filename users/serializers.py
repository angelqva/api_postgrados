from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from users.models import User


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.refresh = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.refresh).blacklist()

        except TokenError:
            self.fail('Bad Token')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'name',
                  'lastname', 'description', 'is_active', 'is_superuser')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}
        }

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """Сериализотор для регистрации пользователя"""
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'password')


class CurrentUserSerializer(serializers.ModelSerializer):
    """Сериализотор для пользователя"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'image', 'password')

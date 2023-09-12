import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from server.apps.user.models import User


from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
                validated_data['email'],
                validated_data['email'],
                validated_data['password']
            )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id email first_name last_name image'.split()

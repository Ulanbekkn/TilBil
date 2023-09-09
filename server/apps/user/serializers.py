import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from server.apps.user.models import User


class RegisterSerializer(serializers.Serializer):
    image = serializers.ImageField(required=False)
    username = serializers.CharField(required=False, default='user')
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8)
    password_check = serializers.CharField(min_length=8)

    @staticmethod
    def validate_password(password):
        if re.match('^(?=.*?[a-z])(?=.*?[0-9]).{8,}$', password):
            return password
        raise ValidationError("The password must consist of at least letters and numbers!")

    def create(self, validated_data):
        username = validated_data.get('username')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('first_name')
        password = validated_data.get('password')
        email = validated_data.get('email')
        image = validated_data.get('image')
        user = User.objects.create_user(username=username, first_name=first_name, password=password, image=image,
                                        email=email, last_name=last_name
                                        )
        user.is_active = False
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id email first_name last_name image'.split()

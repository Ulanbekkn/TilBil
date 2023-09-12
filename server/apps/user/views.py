from django.contrib.auth import authenticate
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from server.apps.user import serializers
from server.apps.user.models import User1
from server.apps.user.serializers import RegisterSerializer, UserSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            'refresh_token': str(refresh),
            'access_token': str(access),
            'expires_in': str(access.lifetime)
        })


class Login(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            return Response(
                {
                    'user': user.username,
                    'refresh_token': str(refresh),
                    'access_token': str(access),
                    'expires_in': str(access.lifetime)
                }
            )
        return Response(data={'Неправильный логин или пароль!'}, status=status.HTTP_401_UNAUTHORIZED)


class UserListView(generics.ListAPIView):
    queryset = User1.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [permissions.AllowAny]

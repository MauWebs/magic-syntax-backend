from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserSerializer, UserSerializerWithToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializers = UserSerializerWithToken(self.user).data
        for token, user in serializers.items():
            data[token] = user
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        try:
            existing_user = User.objects.filter(email=data['email']).first()
            if existing_user:
                message = {'detail': 'El correo electrónico ya está registrado.'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create(
                email=data['email'],
                user_name=data['user_name'],
                password=make_password(data['password']),
            )
            serializer = UserSerializerWithToken(user, many=False)
            return Response(serializer.data)

        except Exception as e:
            message = {'detail': f'Algo salió mal: {str(e)}'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class UsersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        user = request.user
        serializer = UserSerializerWithToken(user, many=False)
        user.user_name = data.get('user_name', user.user_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)
        user.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
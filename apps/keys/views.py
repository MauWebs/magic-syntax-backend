import secrets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import User
from .models import ApiKey
from .serializers import ApiKeySerializer
from .auth import ApiKeyAuthentication


class ApiKeyView(APIView):
    def get(self, request):
        try:
            api_key = ApiKey.objects.get(user=request.user)
            serializer = ApiKeySerializer(api_key)
            return Response(serializer.data)
        except ApiKey.DoesNotExist:
            return Response(
                {'detail': 'API key not found.'}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        api_key, created = ApiKey.objects.get_or_create(user=request.user)
        if not created:
            api_key.key = secrets.token_urlsafe(32)
            api_key.save()
        serializer = ApiKeySerializer(api_key)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ApiKeyInfoView(APIView):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request):
        user = request.user
        try:
            user_data = {
                'email': user.email,
                'user_name': user.user_name,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'start_date': user.formatted_start_date(),
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'plan': user.plan,
            }
            return Response(user_data)
        except User.DoesNotExist:
            return Response(
                {'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND
            )


# from .auth import ApiKeyAuthentication

# class ApiKeyTestView(APIView):
#     authentication_classes = [ApiKeyAuthentication]

#     def get(self, request):
#         if request.user.is_authenticated:
#             return Response('Authenticated user successfully!')
#         else:
#             return Response('Oh no! Unauthenticated user!', status=401)

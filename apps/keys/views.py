from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ApiKey
from .serializers import ApiKeySerializer
from .auth import ApiKeyAuthentication

class ApiKeyView(APIView):
    def get(self, request):
        api_keys = ApiKey.objects.filter(user=request.user)
        serializer = ApiKeySerializer(api_keys, many=True)
        return Response(serializer.data)

    def post(self, request):
        api_key = ApiKey(user=request.user)
        api_key.save()
        serializer = ApiKeySerializer(api_key)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ApiKeyTestView(APIView):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request):
        if request.user.is_authenticated:
            return Response('Authenticated user successfully!')
        else:
            return Response('Oh no! Unauthenticated user!', status=401)

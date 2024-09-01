import secrets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ApiKey
from .serializers import ApiKeySerializer

class ApiKeyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            api_key = ApiKey.objects.get(user=request.user)
            serializer = ApiKeySerializer(api_key)
            return Response(serializer.data)
        except ApiKey.DoesNotExist:
            return Response({"detail": "API key not found."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        api_key, created = ApiKey.objects.get_or_create(user=request.user)
        if not created:
            api_key.key = secrets.token_urlsafe(32)
            api_key.save()
        serializer = ApiKeySerializer(api_key)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

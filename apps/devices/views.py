from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import User
from .serializers import DeviceSerializer
from apps.keys.auth import ApiKeyAuthentication
from datetime import datetime, timezone


class AuthDeviceView(APIView):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request):
        try:
            serializer = DeviceSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(
                {"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception:
            return Response(
                {"error": "Ocurrió un error inesperado."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def put(self, request):
        data = request.data
        user = request.user

        # Imprimir los datos recibidos
        print("Datos recibidos:", data)

        if not user.can_update():
            return Response(
                {
                    "error": "Límite de actualizaciones alcanzado. Intente nuevamente más tarde."
                },
                status=status.HTTP_429_TOO_MANY_REQUESTS,
            )

        serializer = DeviceSerializer(user, data=data, partial=True)

        # Imprimir los datos validados por el serializer
        if serializer.is_valid():
            print("Datos validados:", serializer.validated_data)
            serializer.save(
                last_updated_device=datetime.now(timezone.utc),
                updated_device_count=user.updated_device_count + 1,
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Imprimir los errores del serializer
            print("Errores del serializer:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
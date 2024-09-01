from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.utils.validate_plan import filter_by_plan
from apps.keys.auth import ApiKeyAuthentication, ApiKeyPlan
from .models import Component, ComponentFile
from .serializers import ComponentSerializer, ComponentFileSerializer


class ComponentView(APIView, ApiKeyPlan):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request):
        plan = self.get_user_plan(request)
        print(f"User plan: {plan}")
        components = Component.objects.all()
        print(f"All components: {components}")
        data = filter_by_plan(components, plan)
        print(f"Filtered components: {data}")
        return Response(data)


class ComponentDetailView(APIView):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request, pk):
        plan = self.get_user_plan(request)
        component = get_object_or_404(Component, pk=pk)

        filtered_component = filter_by_plan([component], plan)
        if not filtered_component:
            return Response({'detail': f'You do not have access to this data, your plan is: {plan}'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ComponentSerializer(filtered_component[0])
        return Response(serializer.data)


class ComponentFileView(APIView):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request):
        plan = self.get_user_plan(request)
        files = ComponentFile.objects.all()

        filtered_files = filter_by_plan(files, plan)
        if filtered_files is None:
            return Response({'detail': f'You do not have access to this data, your plan is: {plan}'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ComponentFileSerializer(filtered_files, many=True)
        return Response(serializer.data)


class ComponentFileDetailView(APIView):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request, pk):
        plan = self.get_user_plan(request)
        file = get_object_or_404(ComponentFile, pk=pk)

        filtered_file = filter_by_plan([file], plan)
        if not filtered_file:
            return Response({'detail': f'You do not have access to this data, your plan is: {plan}'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ComponentFileSerializer(filtered_file[0])
        return Response(serializer.data)

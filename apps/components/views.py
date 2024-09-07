from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from core.utils.validate_plan import get_items_by_plan
from apps.keys.auth import ApiKeyAuthentication, ApiKeyPlan
from .models import Component, ComponentFile
from .serializers import ComponentSerializer, ComponentFileSerializer


class ComponentView(APIView, ApiKeyPlan):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request):
        user_plan = self.get_user_plan(request)
        items = get_items_by_plan(user_plan, Component)
        serializer = ComponentSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ComponentDetailView(APIView, ApiKeyPlan):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request, pk):
        user_plan = self.get_user_plan(request)
        item = get_object_or_404(Component, pk=pk, plan__in=self.get_allowed_plans(user_plan))
        serializer = ComponentSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ComponentFileView(APIView, ApiKeyPlan):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request, component_id):
        user_plan = self.get_user_plan(request)
        component = get_object_or_404(Component, pk=component_id, plan__in=self.get_allowed_plans(user_plan))
        items = component.files.all()
        serializer = ComponentFileSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ComponentFileDetailView(APIView, ApiKeyPlan):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request, component_id, pk):
        user_plan = self.get_user_plan(request)
        component = get_object_or_404(Component, pk=component_id, plan__in=self.get_allowed_plans(user_plan))
        item = get_object_or_404(ComponentFile, pk=pk, component=component)
        serializer = ComponentFileSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

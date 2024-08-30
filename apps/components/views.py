from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Component, ComponentFile
from .serializers import ComponentSerializer, ComponentFileSerializer


class ComponentView(APIView):
    def get(self, request):
        components = Component.objects.all()
        serializer = ComponentSerializer(components, many=True)
        return Response(serializer.data)


class ComponentDetailView(APIView):
    def get(self, request, pk):
        component = get_object_or_404(Component, pk=pk)
        serializer = ComponentSerializer(component)
        return Response(serializer.data)


class ComponentFileView(APIView):
    def get(self, request):
        files = ComponentFile.objects.all()
        serializer = ComponentFileSerializer(files, many=True)
        return Response(serializer.data)


class ComponentFileDetailView(APIView):
    def get(self, request, pk):
        file = get_object_or_404(ComponentFile, pk=pk)
        serializer = ComponentFileSerializer(file)
        return Response(serializer.data)

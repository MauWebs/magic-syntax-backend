from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..components.models import Component, ComponentFile
from ..components.serializers import ComponentSerializer, ComponentFileSerializer


class ComponentAdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        components = Component.objects.all()
        serializer = ComponentSerializer(components, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ComponentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComponentDetailAdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        component = get_object_or_404(Component, pk=pk)
        serializer = ComponentSerializer(component)
        return Response(serializer.data)

    def put(self, request, pk):
        component = get_object_or_404(Component, pk=pk)
        serializer = ComponentSerializer(component, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        component = get_object_or_404(Component, pk=pk)
        component.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ComponentFileAdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, component_pk):
        component = get_object_or_404(Component, pk=component_pk)
        files = component.componentfile_set.all()
        serializer = ComponentFileSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request, component_pk):
        component = get_object_or_404(Component, pk=component_pk)
        serializer = ComponentFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(component=component)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComponentFileDetailAdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, component_pk, pk):
        component = get_object_or_404(Component, pk=component_pk)
        file = get_object_or_404(ComponentFile, pk=pk, component=component)
        serializer = ComponentFileSerializer(file)
        return Response(serializer.data)

    def put(self, request, component_pk, pk):
        component = get_object_or_404(Component, pk=component_pk)
        file = get_object_or_404(ComponentFile, pk=pk, component=component)
        serializer = ComponentFileSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, component_pk, pk):
        component = get_object_or_404(Component, pk=component_pk)
        file = get_object_or_404(ComponentFile, pk=pk, component=component)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
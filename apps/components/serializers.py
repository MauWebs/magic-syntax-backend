from rest_framework import serializers
from .models import Component, ComponentFile


class ComponentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentFile
        fields = '__all__'


class ComponentSerializer(serializers.ModelSerializer):
    files = ComponentFileSerializer(many=True, required=False)

    class Meta:
        model = Component
        fields = '__all__'

    def create(self, validated_data):
        files_data = validated_data.pop('files', [])
        component = Component.objects.create(**validated_data)
        for file_data in files_data:
            ComponentFile.objects.create(**file_data)
        return component

from rest_framework import serializers
from .models import Component, ComponentFile


class ComponentFileSerializer(serializers.ModelSerializer):
    plan = serializers.CharField(source='component.plan', read_only=True)

    class Meta:
        model = ComponentFile
        fields = '__all__'


class ComponentSerializer(serializers.ModelSerializer):
    files = ComponentFileSerializer(many=True, required=False)

    class Meta:
        model = Component
        fields = '__all__'

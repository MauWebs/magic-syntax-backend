from rest_framework import serializers
from .models import ApiKey


class ApiKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiKey
        fields = ['id', 'key', 'created_at']
        read_only_fields = ['key', 'created_at']

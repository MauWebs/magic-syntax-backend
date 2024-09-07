from rest_framework import serializers
from apps.users.models import User


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['private_ip', 'mac_address', 'hostname', 'platform', 'arch', 'device_id', 'machine_id', 'last_updated_device', 'updated_device_count']

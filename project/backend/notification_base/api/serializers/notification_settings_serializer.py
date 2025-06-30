from rest_framework import serializers
from notification_base.models import NotificationSettings


class NotificationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSettings
        exclude = ['id', 'user']
        # read_only_fields = ['user']

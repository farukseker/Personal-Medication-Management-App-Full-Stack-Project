from rest_framework import generics, permissions
from notification_base.models import NotificationSettings
from notification_base.api.serializers import NotificationSettingsSerializer


class NotificationSettingsDetailUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = NotificationSettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj, _ = NotificationSettings.objects.get_or_create(user=self.request.user)
        return obj

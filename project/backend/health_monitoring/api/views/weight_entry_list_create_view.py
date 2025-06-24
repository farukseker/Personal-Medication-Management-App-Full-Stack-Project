from rest_framework import generics, permissions
from health_monitoring.models import WeightEntry
from health_monitoring.api.serializers import WeightEntrySerializer
from datetime import date


class WeightEntryListCreateView(generics.ListCreateAPIView):
    serializer_class = WeightEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WeightEntry.objects.filter(
            user=self.request.user
        ).all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

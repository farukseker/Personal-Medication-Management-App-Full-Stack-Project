from rest_framework import generics, permissions
from health_monitoring.models import WeightEntry
from health_monitoring.api.serializers import WeightEntrySerializer



class WeightEntryDeleteView(generics.DestroyAPIView):
    queryset = WeightEntry.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WeightEntrySerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

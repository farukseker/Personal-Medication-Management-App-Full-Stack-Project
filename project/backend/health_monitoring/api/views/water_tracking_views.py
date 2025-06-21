# water/views.py

from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework import permissions, status
from health_monitoring.models import WaterEntry, WaterGoal
from health_monitoring.api.serializers import WaterEntrySerializer, WaterGoalSerializer


class WaterEntryListCreateView(ListCreateAPIView):
    serializer_class = WaterEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WaterEntry.objects.filter(user=self.request.user).order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WaterEntryDeleteView(DestroyAPIView):
    queryset = WaterEntry.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WaterEntrySerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class WaterGoalView(RetrieveUpdateAPIView):
    serializer_class = WaterGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj, created = WaterGoal.objects.get_or_create(user=self.request.user)
        return obj

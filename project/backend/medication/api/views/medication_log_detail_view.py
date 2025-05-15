from rest_framework import generics, permissions
from medication.models import Medication, MedicationSchedule, MedicationLog, DailyNote
from medication.api.serializers import MedicationLogListSerializer


class MedicationLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationLogListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MedicationLog.objects.filter(user=self.request.user)

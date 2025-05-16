from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from medication.api.serializers import MedicationScheduleSerializer
from medication.models import MedicationSchedule


class MedicationScheduleListCreateView(ListCreateAPIView):
    serializer_class =MedicationScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MedicationSchedule.objects.filter(medication__user=self.request.user)

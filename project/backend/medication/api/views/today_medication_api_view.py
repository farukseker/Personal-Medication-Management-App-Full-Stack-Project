from medication.api.serializers import SimpleMedicationScheduleSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from medication.services.medication_timing import MedicationTimeService


class TodayMedicationAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SimpleMedicationScheduleSerializer


    def get_queryset(self, **kwargs):
        meds = MedicationTimeService.for_user_today(self.request.user)
        sorted_data = sorted(meds, key=lambda x: x['time'])
        return sorted_data

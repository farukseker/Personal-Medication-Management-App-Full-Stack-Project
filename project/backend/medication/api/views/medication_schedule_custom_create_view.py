from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from medication.api.serializers import  MedicationScheduleCreateSerializer
from medication.models import MedicationSchedule


class MedicationScheduleCreateView(ListCreateAPIView):
    serializer_class =  MedicationScheduleCreateSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return MedicationSchedule.objects.filter(medication__user=self.request.user)
        return MedicationSchedule.objects.all()

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from medication.api.serializers import MedicationSerializer
from medication.models import Medication


class MedicationListView(ListAPIView):
    serializer_class = MedicationSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user).prefetch_related('schedules')

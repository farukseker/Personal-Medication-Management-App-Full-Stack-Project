from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import localdate, localtime
from medication.api.serializers import MedicationLogListSerializer, MedicationLogSplitListSerializer
from medication.api.mixins import BaseLogMixin


class MedicationLogListCreateView(ListCreateAPIView, BaseLogMixin):
    serializer_class = MedicationLogListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_medication_logs()

    def perform_create(self, serializer):
        data = serializer.validated_data
        # medication_name
        serializer.save(
            user=self.request.user,
            dose_time=data.get('dose_time'),
            medication_name=data.get('medication').name,
            date=localdate(),
            time=localtime()
        )


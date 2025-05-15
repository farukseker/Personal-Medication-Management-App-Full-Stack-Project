from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from medication.api.serializers import MedicationLogCreateSerializer
from medication.models import MedicationLog
from django.utils.timezone import localdate, localtime


class MedicationLogCreateView(CreateAPIView):
    serializer_class = MedicationLogCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MedicationLog.objects.filter(user=self.request.user)

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

from rest_framework.generics import CreateAPIView
from medication_management.api.serializers import MedicationUseHistoryCreateSerializer
from medication_management.models import MedicationUseHistoryModel


class AddMedicationsHistoryView(CreateAPIView):
    serializer_class = MedicationUseHistoryCreateSerializer
    queryset = MedicationUseHistoryModel.objects.all()


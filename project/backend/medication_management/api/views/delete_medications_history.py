from rest_framework.generics import DestroyAPIView
from medication_management.api.serializers import MedicationUseHistoryCreateSerializer
from medication_management.models import MedicationUseHistoryModel


class DeleteMedicationsHistoryView(DestroyAPIView):
    serializer_class = MedicationUseHistoryModel
    lookup_field = 'id'

    def get_queryset(self, *args, **kwargs):
        # user eklenecek
        queryset = MedicationUseHistoryModel.objects.all()
        return queryset

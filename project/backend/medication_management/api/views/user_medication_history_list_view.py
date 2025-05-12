from rest_framework.generics import ListAPIView
from medication_management.models import MedicationModel, MedicationUseHistoryModel
from medication_management.api.serializers import MedicationUseHistoryFlatSerializer
from django.db.models import Prefetch
from datetime import date


class UserMedicationHistoryListView(ListAPIView):
    serializer_class = MedicationUseHistoryFlatSerializer

    def get_queryset(self):
        use_date_str = self.request.query_params.get('use_date')
        target_date = date.fromisoformat(use_date_str) if use_date_str else date.today()

        history_qs = MedicationUseHistoryModel.objects.filter(
            use_date=target_date
        ).select_related('medication').order_by('use_time')
        return history_qs
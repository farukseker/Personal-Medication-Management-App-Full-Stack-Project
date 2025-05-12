from rest_framework.generics import ListAPIView
from medication_management.models import MedicationModel
from medication_management.api.serializers import MedicationListSerializer


class UserMedicationListView(ListAPIView):
    queryset = MedicationModel.objects.all()
    serializer_class = MedicationListSerializer
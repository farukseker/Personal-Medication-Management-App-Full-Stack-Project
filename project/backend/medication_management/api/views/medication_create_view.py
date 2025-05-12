from rest_framework.generics import CreateAPIView
from medication_management.models import MedicationModel
from medication_management.api.serializers import MedicationModelSerializer



class MedicationCreateView(CreateAPIView):
    queryset = MedicationModel.objects.all()
    serializer_class = MedicationModelSerializer

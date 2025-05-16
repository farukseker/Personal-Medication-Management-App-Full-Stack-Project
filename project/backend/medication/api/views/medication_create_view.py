from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from medication.api.serializers import MedicationSerializer
from medication.models import Medication


class MedicationListCreateView(ListCreateAPIView):
    serializer_class = MedicationSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return Medication.objects.filter(user=self.request.user)
        return Medication.objects.all()

    def perform_create(self, serializer):
        print(serializer)
        serializer.save(user=self.request.user)

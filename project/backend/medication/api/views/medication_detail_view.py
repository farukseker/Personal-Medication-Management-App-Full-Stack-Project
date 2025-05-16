from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from medication.api.serializers import MedicationCreateSerializer
from medication.models import Medication


class MedicationDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

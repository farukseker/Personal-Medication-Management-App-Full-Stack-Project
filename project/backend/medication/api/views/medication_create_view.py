from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from medication.api.serializers import MedicationCreateSerializer
from medication.models import Medication


class MedicationCreateView(CreateAPIView):
    serializer_class = MedicationCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

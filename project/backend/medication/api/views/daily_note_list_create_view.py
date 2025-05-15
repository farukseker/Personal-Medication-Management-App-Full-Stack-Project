from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from medication.models import DailyNote
from medication.api.serializers import DailyNoteSerializer


class DailyNoteListCreateView(ListCreateAPIView):
    serializer_class = DailyNoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DailyNote.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

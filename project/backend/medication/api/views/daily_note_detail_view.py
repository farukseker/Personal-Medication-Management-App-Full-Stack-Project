from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from medication.models import DailyNote
from medication.api.serializers import DailyNoteSerializer


class DailyNoteDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DailyNoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DailyNote.objects.filter(user=self.request.user)
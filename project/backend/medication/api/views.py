import datetime
from django.utils.timezone import localdate, localtime

from rest_framework import generics, permissions
from medication.models import Medication, MedicationSchedule, MedicationLog, DailyNote
from .serializers import (
    MedicationSerializer,
    MedicationScheduleSerializer,
    MedicationLogSerializer,
    DailyNoteSerializer,
    SimpleMedicationScheduleSerializer
)

# Medication Views
class MedicationListCreateView(generics.ListCreateAPIView):
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MedicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

# MedicationSchedule Views
class MedicationScheduleListCreateView(generics.ListCreateAPIView):
    serializer_class = MedicationScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MedicationSchedule.objects.filter(medication__user=self.request.user)

class MedicationScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MedicationSchedule.objects.filter(medication__user=self.request.user)

# MedicationLog Views
class MedicationLogListCreateView(generics.ListCreateAPIView):
    serializer_class = MedicationLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MedicationLog.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        data = serializer.validated_data
        # medication_name
        serializer.save(
            user=self.request.user,
            dose_time=data.get('dose_time'),
            medication_name=data.get('medication').name,
            date=localdate(),
            time=localtime()
        )

class MedicationLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MedicationLog.objects.filter(user=self.request.user)


# DailyNote Views
class DailyNoteListCreateView(generics.ListCreateAPIView):
    serializer_class = DailyNoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DailyNote.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DailyNoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DailyNoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DailyNote.objects.filter(user=self.request.user)

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from medication.services.medication_timing import MedicationTimeService


class TodayMedicationAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SimpleMedicationScheduleSerializer


    def get_queryset(self, **kwargs):
        meds = MedicationTimeService.for_user_today(self.request.user)
        sorted_data = sorted(meds, key=lambda x: x['time'])
        return sorted_data

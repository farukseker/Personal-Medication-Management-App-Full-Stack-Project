import datetime
from django.utils.timezone import localdate, localtime
from datetime import timedelta
from rest_framework import generics, permissions
from medication.models import Medication, MedicationSchedule, MedicationLog, DailyNote
from .serializers import (
    MedicationSerializer,
    MedicationScheduleSerializer,
    MedicationLogListSerializer,
    MedicationLogCreateSerializer,
    DailyNoteSerializer,
    SimpleMedicationScheduleSerializer
)

from rest_framework.filters import OrderingFilter

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
    serializer_class = MedicationLogListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if date := self.request.query_params.get('date', None):
            if date == 'today':
                date = localdate()
                return MedicationLog.objects.filter(user=self.request.user, date=date)
            if date == 'yesterday':
                date = localdate() - timedelta(days=1)
                return MedicationLog.objects.filter(user=self.request.user, date=date)
            if date == 'week':
                today = localdate()
                week_start = today  - timedelta(days=today.weekday())
                week_end = week_start + timedelta(days=6)
                return MedicationLog.objects.filter(
                    user=self.request.user,
                    date__range=(week_start, week_end)
                )
            if date == 'month':
                bugun = localdate()
                ay_basi = bugun.replace(day=1)

                # Bir sonraki ayın ilk günü:
                if bugun.month == 12:
                    sonraki_ay_basi = bugun.replace(year=bugun.year + 1, month=1, day=1)
                else:
                    sonraki_ay_basi = bugun.replace(month=bugun.month + 1, day=1)

                ay_sonu = sonraki_ay_basi - timedelta(days=1)
                return MedicationLog.objects.filter(
                    user=self.request.user,
                    date__range=(ay_basi, ay_sonu)
                )


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

class MedicationLogCreateView(generics.CreateAPIView):
    serializer_class = MedicationLogCreateSerializer
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
    serializer_class = MedicationLogListSerializer
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

from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import localdate, localtime
from datetime import timedelta
from medication.api.serializers import MedicationLogListSerializer, MedicationLogSplitListSerializer
from medication.models import MedicationLog
from rest_framework.filters import OrderingFilter


class MedicationLogListCreateView(ListCreateAPIView):
    serializer_class = MedicationLogListSerializer
    permission_classes = [IsAuthenticated]

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

class MedicationLogListView(ListAPIView):
    serializer_class = MedicationLogSplitListSerializer
    permission_classes = [IsAuthenticated]

    def get_medication_logs(self):
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

    def get_queryset(self):
        medication_logs = self.get_medication_logs()
        split_medication_logs = {}
        for medication_log in medication_logs:
            split_medication_logs.setdefault(medication_log.date, [])
            split_medication_logs[medication_log.date].append(medication_log)

        reversed_key: str = 'reverse'
        reversed_param = {
            "true":True,
            "false": False
        } [self.request.query_params.get(reversed_key, 'false')]

        return [{
            "medication_logs": _medication_logs,
            "date": _date
        }
            for _date, _medication_logs in sorted(split_medication_logs.items(), reverse=reversed_param)
        ]


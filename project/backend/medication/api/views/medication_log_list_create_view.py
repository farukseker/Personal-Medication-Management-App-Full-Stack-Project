from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import localdate, localtime
from datetime import timedelta
from medication.api.serializers import MedicationLogListSerializer, MedicationLogSplitListSerializer
from medication.models import MedicationLog
from rest_framework.filters import OrderingFilter


"""
Shit kodun farkındayım ui üzerinde filitreleme için daha uygun bir arayüz uygulandığında bu blok düzeltilecektir  
"""

class MedicationLogListCreateView(ListCreateAPIView):
    serializer_class = MedicationLogListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if filter_type := self.request.query_params.get('date', None):
            if filter_type == 'today':
                date = localdate()
                return MedicationLog.objects.filter(user=self.request.user, date=date)

            if filter_type == 'yesterday':
                date = localdate() - timedelta(days=1)
                return MedicationLog.objects.filter(user=self.request.user, date=date)
            
            if filter_type == 'week':
                today = localdate()
                week_start = today  - timedelta(days=today.weekday())
                week_end = week_start + timedelta(days=6)
                return MedicationLog.objects.filter(
                    user=self.request.user,
                    date__range=(week_start, week_end)
                )

            if filter_type == 'month':
                today = localdate()
                start_of_month = today.replace(day=1)

                # Gelecek ayın ilk günü
                if today.month == 12:
                    start_of_next_month = today.replace(year=today.year + 1, month=1, day=1)
                else:
                    start_of_next_month = today.replace(month=today.month + 1, day=1)

                end_of_month = start_of_next_month - timedelta(days=1)
                return MedicationLog.objects.filter(
                    user=self.request.user,
                    date__range=(start_of_month, end_of_month)
                )

            if filter_type == 'range':
                start_date = self.request.query_params.get('start_date')
                end_date = self.request.query_params.get('end_date') or str(localdate())  # Eğer end_date yoksa bugünün string hali

                if not start_date:
                    raise ValueError("start_date parametresi range filtresi için zorunludur")

                return MedicationLog.objects.filter(
                    user=self.request.user,
                    date__range=(start_date, end_date)
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
        if filter_type := self.request.query_params.get('date', None):
            if filter_type == 'today':
                date = localdate()
                return MedicationLog.objects.filter(user=self.request.user, date=date)

            if filter_type == 'yesterday':
                date = localdate() - timedelta(days=1)
                return MedicationLog.objects.filter(user=self.request.user, date=date)

            if filter_type == 'week':
                today = localdate()
                week_start = today - timedelta(days=today.weekday())
                week_end = week_start + timedelta(days=6)
                return MedicationLog.objects.filter(
                    user=self.request.user,
                    date__range=(week_start, week_end)
                )

            if filter_type == 'month':
                today = localdate()
                start_of_month = today.replace(day=1)

                # Gelecek ayın ilk günü
                if today.month == 12:
                    start_of_next_month = today.replace(year=today.year + 1, month=1, day=1)
                else:
                    start_of_next_month = today.replace(month=today.month + 1, day=1)

                end_of_month = start_of_next_month - timedelta(days=1)
                return MedicationLog.objects.filter(
                    user=self.request.user,
                    date__range=(start_of_month, end_of_month)
                )

            if filter_type == 'range':
                start_date = self.request.query_params.get('start_date')
                end_date = self.request.query_params.get('end_date') or str(
                    localdate())  # Eğer end_date yoksa bugünün string hali

                if not start_date:
                    raise ValueError("start_date parametresi range filtresi için zorunludur")

                return MedicationLog.objects.filter(
                    user=self.request.user,
                    date__range=(start_date, end_date)
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


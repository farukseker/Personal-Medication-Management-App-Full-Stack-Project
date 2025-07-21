from django.db.models import QuerySet
from django.utils.timezone import localdate, localtime
from datetime import timedelta
from medication.models import MedicationLog


class BaseLogMixin:

    def get_medication_logs(self) -> QuerySet[MedicationLog | None]:
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
                end_date = (
                        self.request.query_params.get('end_date')
                        or
                        str(localdate())
                )

                if not start_date:
                    raise ValueError("The start_date parameter is compulsory for range filter")

                return MedicationLog.objects.filter(
                    user=self.request.user,
                    date__range=(start_date, end_date)
                )

        return MedicationLog.objects.filter(user=self.request.user)

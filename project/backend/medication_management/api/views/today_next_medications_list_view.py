from rest_framework.generics import ListAPIView
from datetime import date
from django.db.models import Q
from medication_management.models import MedicationModel
from medication_management.api.serializers import NextReminderSerializer



class TodayNextReminderView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = NextReminderSerializer

    def get_queryset(self):

        today = date.today()
        # user = request.user
        results = []

        medications = MedicationModel.objects.filter(
            Q(start_date__lte=today) &
            Q(end_date__isnull=True) | Q(end_date__gte=today)
            # & Q(user=user)
        ).prefetch_related("reminder", "history", "stages")

        for med in medications:
            history_count = med.history.filter(use_date=today).count()
            reminders = sorted(med.reminder.all(), key=lambda r: r.time)
            next_reminders = reminders[history_count:]

            if med.stages.count() == 1:
                stage = med.stages.first()
            else:
                stage = med.stages.filter(
                    Q(range_start_date__lte=today) &
                    (Q(range_end_date__isnull=True) | Q(range_end_date__gte=today))
                ).order_by("range_start_date").first()

            print(f'{med.name} > {stage} | {bool(stage)} ({len(reminders)})')

            if stage and not reminders:
                results.append({
                    "medication_id": med.id,
                    "medication_name": med.name,
                    "scheduled_time": None,
                    "taken_count": history_count,
                    "reminder_total": 0,
                    "dosage": stage.unit,
                    "dosage_type": stage.unit_type,
                })
            else:
                for reminder in next_reminders:
                    results.append({
                        "medication_id": med.id,
                        "medication_name": med.name,
                        "scheduled_time": reminder.time,
                        "taken_count": history_count,
                        "reminder_total": len(reminders),
                        "dosage": stage.unit,
                        "dosage_type": stage.unit_type,
                    })
        return  results
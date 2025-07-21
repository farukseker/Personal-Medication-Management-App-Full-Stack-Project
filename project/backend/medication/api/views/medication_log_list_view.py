from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from medication.api.serializers import MedicationLogListSerializer, MedicationLogSplitListSerializer
from medication.api.mixins import BaseLogMixin


class MedicationLogListView(ListAPIView, BaseLogMixin):
    serializer_class = MedicationLogSplitListSerializer
    permission_classes = [IsAuthenticated]

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
        } [
            self.request.query_params.get(reversed_key, 'false')
        ]

        return [{
            "medication_logs": _medication_logs,
            "date": _date
        }
            for _date, _medication_logs in sorted(split_medication_logs.items(), reverse=reversed_param)
        ]


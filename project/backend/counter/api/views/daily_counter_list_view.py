from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from django.db.models.functions import TruncDate
from counter.models import CounterEntry
from counter.api.serializers import DailyCounterSerializer
from django.db.models import F


class DailyCounterListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DailyCounterSerializer

    def get_queryset(self):
        return (
            CounterEntry.objects
            .filter(counter__user=self.request.user)
            .annotate(date=TruncDate('timestamp'))
            .values('date', 'counter_id', 'counter__name')
            .annotate(total=Sum('value'))
            .order_by('date')
        )

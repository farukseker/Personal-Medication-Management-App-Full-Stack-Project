from rest_framework import serializers
from counter.models import Counter, CounterEntry


class CounterStatusCreateSerializer(serializers.ModelSerializer):
    # count = serializers.SerializerMethodField(required=False)
    count = serializers.IntegerField(read_only=True)

    # @staticmethod
    # def get_count(i) -> int:
    #     if counts := CounterEntry.objects.filter(counter=i).all():
    #         return sum([count.value for count in counts])
    #     else:
    #         return 0

    class Meta:
        model = Counter
        fields: tuple[str] =  'name', 'unit', 'count'
        # exclude: tuple[str] = 'user',


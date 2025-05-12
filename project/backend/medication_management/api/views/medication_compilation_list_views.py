from rest_framework.generics import ListAPIView
from medication_management.models import MedicationAutoCompilationModel
from medication_management.api.serializers import MedicationAutoCompilationModelSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers


class MedicationCompilationListView(ListAPIView):
    serializer_class = MedicationAutoCompilationModelSerializer
    queryset = MedicationAutoCompilationModel.objects.all()

    @method_decorator(cache_page(60 * 60 * 1))
    @method_decorator(vary_on_cookie)
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

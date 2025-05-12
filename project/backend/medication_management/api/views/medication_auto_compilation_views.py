from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from medication_management.models import MedicationAutoCompilationModel
from medication_management.api.serializers import MedicationAutoCompilationModelSerializer
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError


class CustomSearchFilter(SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_param = request.query_params.get(self.search_param, None)
        if search_param and len(search_param) < 2:
            raise ValidationError("Arama terimi en az 2 karakter olmalıdır.")
        return super().filter_queryset(request, queryset, view)


class MedicationAutoCompilationView(ListAPIView):
    serializer_class = MedicationAutoCompilationModelSerializer
    queryset = MedicationAutoCompilationModel.objects.all()
    filter_backends: tuple = CustomSearchFilter,
    search_fields: tuple = 'name',

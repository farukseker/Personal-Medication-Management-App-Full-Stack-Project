
from django.urls import path, include
from .views import *


app_name = "medication"

urlpatterns = [
    path('create', MedicationCreateView.as_view(), name='create'),
    path('medication-compilation', MedicationAutoCompilationView.as_view(), name='medication-compilation'),
    path('medication-compilation-list', MedicationCompilationListView.as_view(), name='medication-compilation-list'),
    path('add-medications-history', AddMedicationsHistoryView.as_view(), name='add-medications-history'),
    path('delete-medications-history/<int:id>', DeleteMedicationsHistoryView.as_view(), name='delete-medications-history'),
    path('next-medications-list', TodayNextReminderView.as_view(), name='next-medications-list'),
    path('my-medication-history', UserMedicationHistoryListView.as_view(), name='my-medication-list'),
    path('my-medication-list', UserMedicationListView.as_view(), name='my-medication-list'),
]

# özel not



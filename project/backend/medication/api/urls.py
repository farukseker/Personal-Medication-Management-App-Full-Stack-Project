from django.urls import path, include
from .views import (
    MedicationDetailView,
    MedicationScheduleListCreateView, MedicationScheduleDetailView,
    MedicationLogListCreateView, MedicationLogDetailView,
    DailyNoteListCreateView, DailyNoteDetailView,
    TodayMedicationAPIView, MedicationLogCreateView,
    MedicationScheduleCreateView,
    MedicationLogListView,
    MedicationListView, MedicationCreateView
)

app_name = "medication"

urlpatterns = [
    path('medications/', MedicationListView.as_view()),
    path('medications/create/', MedicationCreateView.as_view()),
    path('medications/<int:pk>/', MedicationDetailView.as_view()),

    path('medication-schedules/', MedicationScheduleListCreateView.as_view()),
    path('medication-schedules/<int:pk>/', MedicationScheduleDetailView.as_view()),

    path('medication-logs/', MedicationLogListCreateView.as_view()),
    path('medication-logs/split/', MedicationLogListView.as_view()),
    path('medication-logs/create/', MedicationLogCreateView.as_view()),
    path('medication-logs/<int:pk>/', MedicationLogDetailView.as_view()),

    path('daily-notes/', DailyNoteListCreateView.as_view()),
    path('daily-notes/<int:pk>/', DailyNoteDetailView.as_view()),
    path('today/', TodayMedicationAPIView.as_view()),
]

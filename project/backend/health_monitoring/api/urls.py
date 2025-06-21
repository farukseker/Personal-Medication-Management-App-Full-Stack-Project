from django.urls import path
from health_monitoring.api.views import *

app_name = "health_monitoring_api"

urlpatterns = [
    path('water/entries/', WaterEntryListCreateView.as_view(), name='water-entry-list-create'),
    path('water/entries/<int:pk>/', WaterEntryDeleteView.as_view(), name='water-entry-delete'),
    path('water/goal/', WaterGoalView.as_view(), name='water-goal'),
    path('weight/entries/', WeightEntryListCreateView.as_view(), name='weight-entry'),
    path('weight/entries/<int:pk>/', WeightEntryDeleteView.as_view(), name='weight-entry-delete'),
]

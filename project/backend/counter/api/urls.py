from django.urls import path, include
from .views import (
    CounterListCreateView, CounterTickCreateView
)

app_name = 'counter'

urlpatterns = [
    path('', CounterListCreateView.as_view(), name='counter-list-create'),
    path('tick/', CounterTickCreateView.as_view(), name='counter-tick-create')
]
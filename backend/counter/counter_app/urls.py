from django.urls import path  # type: ignore
from .views import CounterView

urlpatterns = [
    path("/<str:id>/", CounterView.as_view(), name="counter-view"),
]

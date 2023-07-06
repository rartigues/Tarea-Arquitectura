from django.urls import path
from .views import VillainView


urlpatterns = [
    path('registered-villains/', VillainView.as_view()),
]
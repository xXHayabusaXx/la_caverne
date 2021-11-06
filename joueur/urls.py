"""Map URL patterns to view function"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.calcul, name="calcul"),
]

from django.urls import path

from . import views

urlpatterns = [
    path("transactions/detect",view=views.TransactionDetection.as_view()),
]

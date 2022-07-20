from django.urls import path

from . import views

urlpatterns = [
    path("transactions/detect",view=views.TransactionDetection.as_view()),
    path("phishingsite/detect",view=views.PhishingSiteDetection.as_view()),
    path("phishingurl/detect",view=views.PhishingUrlDetection.as_view())
]

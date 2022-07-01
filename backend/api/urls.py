from django.urls import path

from . import views

urlpatterns = [
    path("transactions/",view=views.TransactionListCreateAPIView.as_view()),
    path("transactions/<str:uuid>",view=views.TransactionRetrieveUpdateDestroyAPIView.as_view()),
]

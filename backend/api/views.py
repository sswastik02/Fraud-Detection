from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serialzers import TransactionSerialzier
from .models import Transaction
# Create your views here.
class TransactionListCreateAPIView(ListCreateAPIView):
    """
    (GET|POST) /api/transactions/
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerialzier

class TransactionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    (GET|PUT|PATCH|DELETE) /api/transactions/<str:uuid>
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerialzier
    lookup_field = "uuid"
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Transaction

class TransactionSerialzier(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
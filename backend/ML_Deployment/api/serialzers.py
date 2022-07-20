from rest_framework import serializers
from django.core.validators import MinValueValidator
from decimal import Decimal

class TransactionSerializer(serializers.Serializer):
    merchant_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=20,decimal_places=10,validators=[MinValueValidator(Decimal('0.01'))])
    avg_amount_days = serializers.DecimalField(max_digits=20,decimal_places=10,validators=[MinValueValidator(Decimal('0.01'))])
    is_declined = serializers.BooleanField()
    number_declined_days = serializers.IntegerField(default=0)
    foreign_transaction = serializers.BooleanField()
    high_risk_countries = serializers.BooleanField()
    daily_chbk_avg_amt = serializers.DecimalField(max_digits=10,decimal_places=2)
    sixm_avg_chbk_amt = serializers.DecimalField(max_digits=10,decimal_places=2)
    sixm_chbk_freq = serializers.DecimalField(max_digits=10,decimal_places=2)

class PhishingSerializer(serializers.Serializer):
    url = serializers.URLField()
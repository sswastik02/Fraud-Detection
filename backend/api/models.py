import uuid
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Transaction(models.Model):
    uuid = models.UUIDField(unique=True,default=uuid.uuid4,editable=False)
    merchant_id = models.IntegerField()
    amount = models.DecimalField(max_digits=20,decimal_places=10,validators=[MinValueValidator(Decimal('0.01'))])
    avg_amount_days = models.DecimalField(max_digits=20,decimal_places=10,validators=[MinValueValidator(Decimal('0.01'))])
    is_declined = models.BooleanField()
    number_declined_days = models.IntegerField(default=0)
    foreign_transaction = models.BooleanField()
    high_risk_countries = models.BooleanField()
    daily_chbk_avg_amt = models.DecimalField(max_digits=10,decimal_places=2)
    sixm_avg_chbk_amt = models.DecimalField(max_digits=10,decimal_places=2)
    sixm_chbk_freq = models.DecimalField(max_digits=10,decimal_places=2)
    

from django.db import models
from datetime import datetime


class Base_rates(models.Model):
    
    date = models.CharField(max_length=20)
    usd_value = models.CharField(max_length=5)
    eur_value = models.CharField(max_length=5)
    jpy_value = models.CharField(max_length=5)
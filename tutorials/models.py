import datetime

from django.db import models


class Tutorial(models.Model):
    scrip_name = models.CharField(max_length=100, default="Unknown")
    trade_date = models.DateTimeField(default=datetime.datetime.today(), null=False)
    quantity = models.IntegerField(default=1, null=False)
    price = models.DecimalField(default=0.0, max_digits=20,
                         decimal_places=2, null=False)
    trade_value = models.DecimalField(default=0.0, max_digits=20,
                         decimal_places = 2, null=False)
    order_type = models.CharField(max_length=60, default="Buy")
from django.db import models
from currencies import CurrencyRate

class CurrencyRate(models.Model):
    """Class representing currency exchange rates"""

    # Fields
    currency_id = models.ForeignKey(CurrencyRate, on_delete=models.CASCADE)
    base_currency_id = models.ForeignKey(CurrencyRate, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=16, decimal_places=6)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.currency_id
from django.db import models

# Create your models here.
class Currency(models.Model):
    """Class representing currencies saved in db"""

    # Fields
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=128)
    is_base_currency = models.BooleanField()

    def __str__(self):
        return self.code
    
class CurrencyRate(models.Model):
    """Class representing currency exchange rates"""

    # Fields
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_id')
    base_currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='base_currency_id')
    rate = models.DecimalField(max_digits=16, decimal_places=6)
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.currency_id) + ' at ' + str(self.timestamp)
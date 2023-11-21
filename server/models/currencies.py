from django.db import models

class CurrencyRate(models.Model):
    """Class representing currencies saved in db"""

    # Fields
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=128)
    is_base_currency = models.BooleanField()

    def __str__(self):
        return self.code
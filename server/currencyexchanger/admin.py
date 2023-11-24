from django.contrib import admin

from currencyexchanger.models import Currency, CurrencyRate

# Register your models here.
admin.site.register(Currency)
admin.site.register(CurrencyRate)
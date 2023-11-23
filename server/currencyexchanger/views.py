from django.http import JsonResponse
from currencyexchanger.models import Currency

# Create your views here.
def showCurrencies(request):
    all_currencies = list(Currency.objects.values("code"))
    return JsonResponse(all_currencies, status=200, safe=False)
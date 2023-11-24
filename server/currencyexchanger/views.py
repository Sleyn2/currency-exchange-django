from decimal import Decimal
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from currencyexchanger.models import Currency, CurrencyRate
import yfinance as yf

def getCurrency(request, *args, **kwargs):
    all_currencies = list(Currency.objects.values("code"))
    return JsonResponse(all_currencies, status=200, safe=False)

def getCurrencyRate(request, currency_1, currency_2, *args, **kwargs):
    if not Currency.objects.filter(code=currency_1).exists():
        return HttpResponseBadRequest('Selected currency isn\'t listed in database: ' + currency_1, status=400)
    if not Currency.objects.filter(code=currency_2).exists():
        return HttpResponseBadRequest('Selected currency isn\'t listed in database: ' + currency_2, status=400)
    
    rate_1 = getRate(currency_1)
    rate_2 = getRate(currency_2)

    final_rate = rate_1*rate_2

    return JsonResponse(final_rate, status=200, safe=False)

def loadstock(request):
    if not CurrencyRate.objects.exists():
        usd = Currency.objects.get(code='USD')
        for currency in Currency.objects.all():
            data = yf.download(str(currency)+'=x', start='2023-09-01', end='2023-11-24')
            for index, row in data.iterrows():
                obj = CurrencyRate(currency_id=currency, base_currency_id=usd, rate=row['Close'], timestamp=index.strftime('%Y-%m-%d'))
                obj.save()
                print(index.strftime('%Y-%m-%d') + str(currency))
    else:
        return HttpResponseBadRequest('Data already downloaded', status=400)
    return HttpResponse('Data downloaded', status=200)

def getRate(currency):
    if(currency == 'USD'):
        return Decimal(1.0)
    else:
        x = CurrencyRate.objects.all().filter(currency_id=Currency.objects.get(code=currency)).order_by('-timestamp')[0]
        return x.rate

def price(ticker, period='30d',columns=['Close']):
    '''
    Returns a DataFrame of prices for ticker from Yahoo Finance API 
    '''
    obj = yf.Ticker(str(ticker)+'=x')
    print(str(ticker)+':')
    print(obj.info['regularMarketPreviousClose'])
    return obj.history(period=period)[columns]
from django.conf import settings


def currency_info(request):
    return {'currency_symbol': settings.CURRENCY.symbol, 'currency_code': settings.CURRENCY.code}

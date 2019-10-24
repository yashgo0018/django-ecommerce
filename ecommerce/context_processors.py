from django.conf import settings


def currency_info(request):
    return {'currency_symbol': settings.currency.symbol, 'currency_code': settings.currency.code}

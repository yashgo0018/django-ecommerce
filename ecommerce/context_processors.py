from django.conf import settings


def currency_info(request):
    return {'currency_symbol': settings.get('currency').get('symbol'), 'currency_code': settings.get('currency').get('code')}

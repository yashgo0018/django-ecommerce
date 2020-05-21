from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'HOST': os.environ.get('DB_HOST'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'USER': os.environ.get('DB_USER'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

SECRET_KEY = 'ly19&2+c#onohxpodxnrlpvx3#)wc_qw!nvnb0^)oe%_yj$vf4'
ALLOWED_HOSTS = ['ecommerce.pythonanywhere.com']

MEDIA_ROOT = '/home/ecommerce/ecommerce/media'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/ecommerce/ecommerce/static'
STATIC_URL = '/static/'

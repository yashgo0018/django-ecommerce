# import dj_database_url
from .base import *

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# INSTALLED_APPS.insert(INSTALLED_APPS.index(
#     'django.contrib.staticfiles') - 1, 'whitenoise.runserver_nostatic')

# DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

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


STATIC_URL = '/static/'

MEDIA_ROOT = '/home/ecommerce/ecommerce/media'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/ecommerce/ecommerce/static'
STATIC_URL = '/static/'

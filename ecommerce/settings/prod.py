import dj_database_url
from .base import *

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

INSTALLED_APPS.insert(INSTALLED_APPS.index(
    'django.contrib.staticfiles') - 1, 'whitenoise.runserver_nostatic')

DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

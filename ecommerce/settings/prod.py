import dj_database_url
from .base import *

STATICFILES_STORAGE = 'ecommerce.storage.WhiteNoiseStaticFilesStorage'

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

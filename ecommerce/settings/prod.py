import dj_database_url
import django_heroku
from .base import *

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

DATABASES['default'].update(dj_database_url.config(conn_max_age=500))
django_heroku.settings(locals())

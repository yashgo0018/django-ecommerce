import dj_database_url

from .base import *

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

# Add Your Razorpay keys
RAZORPAY_KEY_ID = 'rzp_test_Xs4cMHfADoX6DU'
RAZORPAY_KEY_SECRET = 'MzgRhzXb5bVJYqUPVHAdEOhR'

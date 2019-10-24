import dj_database_url
from google.oauth2 import service_account

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost:5000', 'python-ecom-app.herokuapp.com']

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES = {
    'default': prod_db
}

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

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Add Your Razorpay keys
RAZORPAY_KEY_ID = 'rzp_test_Xs4cMHfADoX6DU'
RAZORPAY_KEY_SECRET = 'MzgRhzXb5bVJYqUPVHAdEOhR'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

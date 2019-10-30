from .base import *
import dj_database_url

# Add Your Razorpay keys
RAZORPAY_KEY_ID = 'rzp_test_Xs4cMHfADoX6DU'
RAZORPAY_KEY_SECRET = 'MzgRhzXb5bVJYqUPVHAdEOhR'
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2'
}
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

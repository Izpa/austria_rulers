# SECURITY WARNING: keep the secret key used in production secret!
import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'l7$yypbafdsg)e7$n@asfsdbzbn@sdfv8hwl57n74asd,3du=y9r8_03vw@k6iy0c4q')

# Allow all host headers
ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

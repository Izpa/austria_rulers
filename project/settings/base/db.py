import os
import dj_database_url

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'austria_rulers',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

if os.environ.get('DATABASE_URL', False):
    # Change 'default' database configuration with $DATABASE_URL.
    DATABASES['default'] = dj_database_url.config(conn_max_age=500)

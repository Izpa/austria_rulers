import os

opbeat_organization_id = os.environ.get('OPBEAT_ORGANIZATION_ID')
opbeat_app_id = os.environ.get('OPBEAT_APP_ID')
opbeat_secret_token = os.environ.get('OPBEAT_SECRET_TOKEN')

if opbeat_organization_id and opbeat_app_id and opbeat_secret_token:

    INSTALLED_APPS = INSTALLED_APPS + ('opbeat.contrib.django', )

    OPBEAT = {
        'ORGANIZATION_ID': opbeat_organization_id,
        'APP_ID': opbeat_app_id,
        'SECRET_TOKEN': opbeat_secret_token,
        'DEBUG': True if os.environ.get('OPBEAT_DEBUG', False) else False,
    }

    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('opbeat.contrib.django.middleware.OpbeatAPMMiddleware', )

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'opbeat': {
                'level': 'WARNING',
                'class': 'opbeat.contrib.django.handlers.OpbeatHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'site': {
                'level': 'WARNING',
                'handlers': ['opbeat'],
                'propagate': False,
            },
            'opbeat.errors': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'console_warnings': {
                'level': 'INFO',
                'handlers': ['console'],
                'propagate': False
            }
        },
    }

# Best place to change this env variables is project/settings/local_env.py file. It loads after this one specially to
# allow you manage env without touching project code.
import os

DEVELOPMENT = 'development'
STAGING = 'staging'
PRODUCTION = 'production'
PROJECT_NAME = 'austria-rulers'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000

LOCATION = os.environ.get('LOCATION', None)

if LOCATION == DEVELOPMENT:
    DEBUG = True
    HOSTNAME = ''
elif LOCATION == STAGING:
    DEBUG = False
    HOSTNAME = ''
elif LOCATION == PRODUCTION:
    DEBUG = False
    HOSTNAME = ''
else:
    LOCATION = 'local'
    DEBUG = True
    HOSTNAME = False

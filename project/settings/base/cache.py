import os
from urllib.parse import urlparse

redis_url = os.environ.get('REDIS_URL', None)
if redis_url:
    redis_url = urlparse(redis_url)

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "{scheme}://{hostname}:{port}".format(scheme=redis_url.scheme,
                                                              hostname=redis_url.hostname,
                                                              port=redis_url.port),
            "OPTIONS": {
                "PASSWORD": redis_url.password,
                "DB": 0,
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }

else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'localhost:11211',
        }
    }

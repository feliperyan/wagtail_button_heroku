from .base import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


DEBUG = False
TEMPLATE_DEBUG = False


try:
    from .local import *
except ImportError:
    pass

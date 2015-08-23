from .base import *
import os

import dj_database_url

DATABASES['default'] = dj_database_url.config()
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

DEBUG = True
TEMPLATE_DEBUG = True

# --- Getting environment variables set in Heroku ---
SECRET_KEY = os.environ.get('SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_BUCKET')
AWS_ACCESS_KEY_ID =  os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY =  os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# --- Using whiteboise for Static Files ---
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'


try:
    from .local import *
except ImportError:
    pass

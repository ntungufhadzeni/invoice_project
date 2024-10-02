from .base import *

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")

HOST = os.environ.get('HOST', '')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')

CSRF_TRUSTED_ORIGINS = ['https://*.' + HOST, ]

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_USER')
EMAIL_USE_TLS = False  # Use TLS encryption
EMAIL_USE_SSL = True  # Use SSL (False if you're using TLS)

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

from django.conf import settings

######### Use AWS S3 storage media files ##########
AWS_ACCESS_KEY_ID = getattr(settings, 'AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = getattr(settings,'AWS_SECRET_ACCESS_KEY')
DEFAULT_FILE_STORAGE = getattr(settings, 'DEFAULT_FILE_STORAGE', 'storages.backends.s3boto.S3BotoStorage')
AWS_STORAGE_BUCKET_NAME = getattr(settings, 'AWS_STORAGE_BUCKET_NAME')
ASSETS_URL = getattr(settings, 'ASSETS_URL')
MEDIA_ROOT = ASSETS_URL + 'media/'
MEDIA_URL = ASSETS_URL + 'media/'
AWS_S3_SECURE_URLS = getattr(settings, 'AWS_S3_SECURE_URLS', True)
AWS_QUERYSTRING_AUTH = getattr(settings, 'AWS_QUERYSTRING_AUTH', True)

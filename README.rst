========================
AWS S3 Files Manager
========================

An AWS S3 Files online manager base on python/django

To use this app follow these steps:

#. Create your working environment
#. Install Django
#. Put the s3filesmanager into INSTALLED_APPS
#. Install additional dependencies
#. syncdb and migrate (if you use South)

Install
=======
::

    pip install s3filesmanager


Dependency
==========

#. django-model-utils
#. django-bootstrap-toolkit
#. PIL
#. sorl-thumbnail
#. boto
#. django-storages


INSTALLED_APPS
==============
::

    INSTALLED_APPS = (
        ...
        'south',
        'bootstrap_toolkit',
        'sorl.thumbnail',
        's3filesmanager',
    )


Settings
===================
::

    AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEY_ID'
    AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_ACCESS_KEY'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_STORAGE_BUCKET_NAME = 'YOUR_AWS_STORAGE_BUCKET_NAME'
    ASSETS_URL = 'https://BUCKET_NAME.stimuli.s3-website-us-east-1.amazonaws.com'
    MEDIA_ROOT = ASSETS_URL + 'media/'
    MEDIA_URL = ASSETS_URL + 'media/'
    AWS_S3_SECURE_URLS = False
    AWS_QUERYSTRING_AUTH = False


urls.py
=======
::

    url(r'^', include('s3filesmanager.urls')),


template tags
=============
::

    {% load s3filesmanager_tags %}

    <!-- Put the s3filesmanager tag in a div which you want to show the files manager -->
    <div>
        {% s3filesmanager %}
    </div>

    <!-- Put the s3filesmanager_js tag in html head, but need to load jquery and bootstrap at first -->
    <script src="http://code.jquery.com/jquery-latest.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
    {% s3filesmanager_js %}


Javascript
==========

The app use some javascript lib for upload files

#. jQuery
#. Bootstrap
#. plupload
#. Underscore


Sponsor
=======

Sponsored by www.xperiment.mobi

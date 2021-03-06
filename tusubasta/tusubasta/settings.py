"""
Django settings for tusubasta project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')x2=7i0721d$fk55==ze%4c982a5bqnbi0m-iruv(n&&u_!%!e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'sitio',
    'login',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'tusubasta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tusubasta.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tusubasta_BD',
        'USER': 'usrsubasta',
        'PASSWORD': 'subasta01',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#Configuracion para Amazon

STATICFILES_LOCATION = '/static/'

MEDIAFILES_LOCATION = 'media'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_S3_SECURE_URLS = False

AWS_STORAGE_BUCKET_NAME = "tusubasta"

AWS_S3_CUSTOM_DOMAIN = 's3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME

#STATIC_URL = "https://s3.amazonaws.com/%s/" % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://s3.amazonaws.com/tusubasta/%s/" % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = "https://%s/il/media/" % AWS_S3_CUSTOM_DOMAIN

AWS_QUERYSTRING_AUTH = False

AWS_DEFAULT_ACL = "private"

from boto.s3.connection import ProtocolIndependentOrdinaryCallingFormat

AWS_S3_CALLING_FORMAT = ProtocolIndependentOrdinaryCallingFormat()

from boto.s3.connection import S3Connection

S3Connection.defaultHost = 's3-us-east-1.amazon.com'

#STATICFILES_DIR = [os.path.join(BASE_DIR,"static/"),
# "/home/aimhoff/.virtualenvs/ingweb/Documentos/Ingenieria\ Web/tusubasta/static/"]

AWS_ACCESS_KEY_ID = "AKIAIAHFC2ZDTYRBFWWQ"

AWS_SECRET_ACCESS_KEY = "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"

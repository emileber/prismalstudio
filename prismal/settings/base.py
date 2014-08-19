"""
Django settings for prismal project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
import sys
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.normpath(os.path.dirname(os.path.abspath(__file__) ) + "/..")
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z%140qb^bb@otgl#j5w65rfk-56+v%9%z#+ci9isvr5b&%9*%w'

# SECURITY WARNING: don't run with debug turned on in production!

TEMPLATE_DEBUG = True


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'bootstrap3',
    'jquery',
    'resume',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    'solid_i18n.middleware.SolidLocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware', # only in prod
)

ROOT_URLCONF = 'prismal.urls'

WSGI_APPLICATION = 'prismal.wsgi.application'

# Parse database configuration from $DATABASE_URL

DATABASES = {'default': dj_database_url.config()}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

#LANGUAGE_CODE = 'en-us'
ugettext_lazy = lambda s: s
LANGUAGES = (
    ('fr', ugettext_lazy('French')),
    ('en', ugettext_lazy('English')),
)
LANGUAGE_CODE = 'fr'

# Optional. If you want to use redirects, set this to True
SOLID_I18N_USE_REDIRECTS = False

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    #"django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    #"django.core.context_processors.media",
    #"django.core.context_processors.static",
    #"django.core.context_processors.tz",
    #"django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'prismal.context_processors.solid_i18n',
)


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Static asset configuration

STATIC_ROOT = 'staticfiles'


STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

SUIT_CONFIG = {
    'ADMIN_NAME': 'Prismal Studio',
}

BOOTSTRAP3 = {'jquery_url': STATIC_URL + "js/jquery.js", }

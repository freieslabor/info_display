"""
Django settings for info_display project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import logging
import os

settings_logger = logging.getLogger('info-display.settings')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ntd)j#j$9ulu!!l16bi7ukq--2c^n$ujlfi1@2sde0m!e&_3=2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('INFO_DISPLAY_DEBUG', False)

settings_logger.debug('DEBUG={}'.format(bool(DEBUG)))

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'info_display',

    # django suit
    'suit',
    'suit_ckeditor',

    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # screens
    'info_display.screens.days_without_an_accident',
    'info_display.screens.public_transport_schedule',
    'info_display.screens.event_schedule',
)

if DEBUG:
    try:
        import django_extensions

        INSTALLED_APPS += (
            'django_extensions',
        )

    except ImportError:
        pass

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

ROOT_URLCONF = 'info_display.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'info_display.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASE_NAME = os.environ.get('INFO_DISPLAY_DB', 'data/db.sqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_NAME,
    }
}

settings_logger.debug('DATABASE={}'.format(DATABASE_NAME))


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'
DATETIME_FORMAT = 'D j. N H:i:s'
DATE_FORMAT = 'D j. N'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('INFO_DISPLAY_STATIC_ROOT', 'data/static')

settings_logger.debug('STATIC_ROOT={}'.format(STATIC_ROOT))

# Django Suit
SUIT_CONFIG = {
    'ADMIN_NAME': 'Info Display',
    'HEADER_DATE_FORMAT': 'D j. N',
    'HEADER_TIME_FORMAT': 'H:i',

    'MENU': (
        'sites',
        {
            'app': 'auth',
            'label': 'Auth',
            'icon': 'icon-lock',
            'models': ('user', 'group'),
        },
        {
            'label': 'Main Screen',
            'icon': 'icon-th-large',
            'url': '/main-screen/',
        },
        '-',
        # {
            # 'app': 'announcer',
            # 'label': 'Announcer',
            # 'icon': 'icon-info-sign',
        # },
        {
            'app': 'days_without_an_accident',
            'label': 'Days Without An Accident',
            'icon': 'icon-fire',
        },
        {
            'app': 'public_transport_schedule',
            'label': 'Public Transport Schedule',
            'icon': 'icon-road',
        },
        {
            'app': 'event_schedule',
            'label': 'Event Schedule',
            'icon': 'icon-calendar',
        },
    ),
}

# info display
INFO_SCREEN_SCREENS = (
    '/screens/days_without_an_accident/',
    '/screens/public_transport_schedule/25721026/',
    '/screens/event_schedule/',

    #http://andreas-seier.eu/bahn/a.html
    'https://iris.noncd.db.de/wbt/js/index.html?typ=ab&bhf=8000169&bhfname=&zugtyp=&platform=&zeilen=10&paging=1&pagingdauer=10&via=0&impressum=0&style=&lang=de&SecLang=en',
)

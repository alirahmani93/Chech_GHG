import os
from pathlib import Path

from django.contrib.staticfiles.finders import AppDirectoriesFinder
from dotenv import load_dotenv, find_dotenv

env_file = Path(find_dotenv(usecwd=True))
load_dotenv(verbose=True, dotenv_path=env_file)
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-w34#+sf(hziskp3wbl6!t*(8^6!)s@#(8yeofk5ebgccfkd)=_'

DEBUG = True

INTERNAL_IPS = ['127.0.0.1', ]

ALLOWED_HOSTS = []

THOUSAND_SEPARATOR = True #### mohem ####

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    "debug_toolbar",  ## In debug mode
    "azbankgateways",

    "users",
    "product",
    # "cart",
    # "shipping",
    # "wallet",
    # "payment",

]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chech_GHG.urls'
AUTH_USER_MODEL = 'users.OurUser'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'chech_GHG.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = ((BASE_DIR / 'static/'),)

MEDIA_ROOT = '/media/'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#### ____________  my custom setting  ____________ ####
AZ_IRANIAN_BANK_GATEWAYS = {
    'GATEWAYS': {
        'BMI': {
            'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
            'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
            'SECRET_KEY': '<YOUR SECRET CODE>',
        },
        'SEP': {
            'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
            'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
        },
        'ZARINPAL': {
            'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        },
        'IDPAY': {
            'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
            'METHOD': 'POST',  # GET or POST
            'X_SANDBOX': 0,  # 0 disable, 1 active
        },
        'ZIBAL': {
            'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        },
        'BAHAMTA': {
            'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        },
        'MELLAT': {
            'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
            'USERNAME': '<YOUR USERNAME>',
            'PASSWORD': '<YOUR PASSWORD>',
        },
    },
    'DEFAULT': 'BMI',
    'CURRENCY': 'IRR',  # اختیاری
    'TRACKING_CODE_QUERY_PARAM': 'tc',  # اختیاری
    'TRACKING_CODE_LENGTH': 16,  # اختیاری
    'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader',  # اختیاری

    'BANK_PRIORITIES': [
        'BMI',
        'SEP',
    ],
}

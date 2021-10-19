import os
from datetime import timedelta
from pathlib import Path

import django_redis.client
from django.contrib.staticfiles.finders import AppDirectoriesFinder
from dotenv import load_dotenv, find_dotenv

# from celery.schedules import crontab

env_file = Path(find_dotenv(usecwd=True))
load_dotenv(verbose=True, dotenv_path=env_file)
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True
INTERNAL_IPS = ['127.0.0.1', ]
ALLOWED_HOSTS = []

THOUSAND_SEPARATOR = True  #### mohem ####

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # "debug_toolbar",  ## In debug mode
    "rest_framework",
    # "rest_framework.authtoken",
    # "rest_framework_simplejwt",

    'django_filters',

    "product",
    "users",
    "cart",
    "payment",
    "chech_GHG",

    # "shipping",
    # "wallet",

]

MIDDLEWARE = [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1/day',
        'user': '10/day'
    },
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

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

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6380/0",
        "TIMEOUT": 60 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "bbbarghi"
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

STATIC_URL = 'static/'
# STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = ((BASE_DIR / 'static/'),)

# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# ]
MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_URL = 'media/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'
# LOGIN_URL = '/login/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_USERNAME")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")

CRISPY_TEMPLATE_PACK = 'bootstrap4'

KAVENAGAR_API_KEY = os.environ.get("KAVENAGAR_API_KEY")

CELERY_BROKER_URL = 'redis://localhost:6380/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6380/2'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Tehran'

CELERY_BEAT_SCHEDULE = {
    "hello_task": {
        # "task": "product_present.tasks.hello_task",
        # # "schedule": crontab(minute="*/1"),
        # "schedule": 10.0,
        # "args": ("ashkan",),
    },
    "hello_ghamar": {
        # "task": "product_present.tasks.hello_task",
        # "schedule": crontab(minute="*/1"),
        # # "schedule": 10.0,
        # "args": ("ghamar",),
    }
}

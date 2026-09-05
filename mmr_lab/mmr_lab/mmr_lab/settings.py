"""
Django settings for mmr_lab project.
"""

from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-^i396%c8#o)!lb!pojvrf5ut0ju)#yufla%p@z041s&)(xkuk_'



DEBUG = True



ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
]



# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'website',
    'research',

]



MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]



ROOT_URLCONF = 'mmr_lab.urls'



TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'website/templates'
        ],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

                'research.context_processors.team_members',

            ],

        },

    },

]



WSGI_APPLICATION = 'mmr_lab.wsgi.application'



# Database

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }

}



# Password validation

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



# Language

LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'Asia/Dhaka'


USE_I18N = True


USE_TZ = True



# Static files

STATIC_URL = '/static/'


STATIC_ROOT = BASE_DIR / "staticfiles"



# Media files

MEDIA_URL = '/media/'


MEDIA_ROOT = BASE_DIR / 'media'



# Default primary key

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
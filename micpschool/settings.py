"""
Django settings for micpschool project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# micpschool_less = os.path.join(BASE_DIR, 'micpschool', 'static', 'less')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
# For apps outside of your project, it's simpler to import them to find their root folders

#bootstrap_less = os.path.join(os.path.dirname(twitter_bootstrap.__file__), 'static', 'less')
#PIPELINE_LESS_ARGUMENTS = u'--include-path={}'.format(os.pathsep.join([bootstrap_less, micpschool_less]))
# SECURITY WARNING: keep the secret key used in production secret!
# try:
#     if("SECRET_KEY" in os.environ['SECRET_KEY']):
#         SECRET_KEY = os.environ['SECRET_KEY']
# except KeyError:
#         SECRET_KEY ='_23=-7y*)(zkp^x8ha&p3k0w*ctqbhp1f@^fiexs!3zq&op%hh'
# else:
SECRET_KEY ='_23=-7y*)(zkp^x8ha&p3k0w*ctqbhp1f@^fiexs!3zq&op%hh'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'www.micpschool.com','chainuser1.pythonanywhere.com']
# CACHES = {
    # "default": {
    #     "BACKEND": "django_redis.cache.RedisCache",
    #     "LOCATION": "redis://127.0.0.1:6379/",
    #     "OPTIONS": {
    #         "CLIENT_CLASS": "django_redis.client.DefaultClient",
    #         "PASSWORD": "",
    #         "CLIENT_CLASS": "django_redis.client.DefaultClient",
    #         "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
    #         "SOCKET_TIMEOUT": 5,  # in seconds
    #     },
    #     "KEY_PREFIX": "example"
    # }
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
BROKER_URL = 'amqp://guest:guest@localhost:5672//'


# Application definition

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_humanize',
    'bootstrap4',
     'news',
     'django_ajax',
     'exams',
     'login',
     'static',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'micpschool.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'micpschool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'micpschool',
    #     'USER': 'root',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # }
    # 'default':{
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME':'micpschool',
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
    #         'charset': 'utf8mb4',
    #     },
    #      'TEST': {
    #         'CHARSET': 'utf8mb4',
    #         'COLLATION': 'utf8mb4_unicode_ci',
    #     },
    #     'USER': 'root',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# STATIC_URL ='/static/'
# STATIC_ROOT = "/home/chainuser1/micpschool/static"
# # or, eg,

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL ='/static/'
# STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
#
#
# PIPELINE_COMPILERS = (
#     'pipeline.compilers.less.LessCompiler',
# )
#
#
#
#
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


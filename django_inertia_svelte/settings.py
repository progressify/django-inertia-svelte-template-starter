from pathlib import Path
from configurations import Configuration

import os


class Base(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-j3^^k66udp0o2w69c(i$zg(20&4*is=^$tw&)r@fm-r(eb&2zr'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    # Application definition
    INSTALLED_APPS = [  # django apps
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles'
    ]
    INSTALLED_APPS += [  # library apps
        'inertia',
        'django_vite',
    ]
    INSTALLED_APPS += [  # project apps
        'sample_app',
        'another_app'
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django_inertia_svelte.middleware.InertiaShare',
        'inertia.middleware.InertiaMiddleware',
    ]

    ROOT_URLCONF = 'django_inertia_svelte.urls'
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
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

    WSGI_APPLICATION = 'django_inertia_svelte.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases
    @property
    def DATABASES(self):
        return self.get_databases_setting()

    def get_databases_setting(self):
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': self.BASE_DIR / 'db.sqlite3',
            }
        }

    # Password validation
    # https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
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
    # https://docs.djangoproject.com/en/4.1/topics/i18n/
    LANGUAGE_CODE = 'it-IT'
    TIME_ZONE = 'Europe/Rome'
    USE_I18N = True
    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/
    STATIC_ROOT = BASE_DIR / "collectedstatic"
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(BASE_DIR.parent, 'media')
    MEDIA_URL = '/media/'

    # Where ViteJS assets are built.
    DJANGO_VITE_ASSETS_PATH = BASE_DIR / "static" / "dist"

    # If use HMR or not.
    DJANGO_VITE_DEV_MODE = DEBUG

    # Include DJANGO_VITE_ASSETS_PATH into STATICFILES_DIRS to be copied inside
    # when run command python manage.py collectstatic
    STATICFILES_DIRS = [
        DJANGO_VITE_ASSETS_PATH,
        BASE_DIR / "static" / "assets"
    ]

    INERTIA_LAYOUT = 'base.html'

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    # logger configuration
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(levelname)s [%(name)s]: %(asctime)s %(message)s',
                'datefmt': '%d-%m-%Y %H:%M:%S',
            },
            'color': {
                '()': 'colorlog.ColoredFormatter',
                'format': '%(log_color)s    %(levelname)s [%(name)s]: %(asctime)s %(message)s',
                'datefmt': '%d-%m-%Y %H:%M:%S',
                'log_colors': {
                    'DEBUG': 'white',
                    'INFO': 'cyan',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'bold_black,bg_white'
                },
            },
        },
        'handlers': {
            'color_console': {
                'class': 'logging.StreamHandler',
                'formatter': 'color',
            },
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 1024 * 1024 * 10,  # 20 MB
                'backupCount': 2,
                'formatter': 'simple',
                'filename': os.path.join(BASE_DIR.parent, 'debug.log'),
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
            },
        },
        'loggers': {
            '': {
                'handlers': ['color_console', 'file'],
                'propagate': True,
                'level': 'DEBUG',
            },
            'botocore': {'handlers': ['file'], 'propagate': False, 'level': 'DEBUG'},
            'boto3': {'handlers': ['file'], 'propagate': False, 'level': 'DEBUG'},
            's3transfer': {'handlers': ['file'], 'propagate': False, 'level': 'DEBUG'},
            'urllib3': {'handlers': ['file'], 'propagate': False, 'level': 'DEBUG'}
        }
    }

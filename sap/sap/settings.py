"""
Django settings for sap project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from __future__ import absolute_import
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from unipath import Path
RUTA_PROYECTO = Path(__file__).ancestor(2)


CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
CELERY_BEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jn%_^&vo#*x5#uwkig51-ai4l)8e@lj5zurf6n8u_a+_jh$gw4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#En este path se almacenaran los archivos externos y las imagenes que carguen
#los usuarios del sistema

MEDIA_ROOT = Path(__file__).ancestor(2) + '/static/uploads/'
MEDIA_URL = '/uploads/'

#Ruta de configuraciones de Celery
BROKER_URL = "amqp://sap:sap@localhost:5672/sap"

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'aplicaciones.usuarios',
    'aplicaciones.roles',
    'aplicaciones.proyectos',
    'aplicaciones.fases',
    'aplicaciones.tipoatributo',
    'aplicaciones.tipoitem',
    'aplicaciones.items',
    'aplicaciones.relaciones',
    'aplicaciones.lineabase',
    'aplicaciones.solicitudes',
    'aplicaciones.comite',
    'aplicaciones.informes',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'sap.urls'

WSGI_APPLICATION = 'sap.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'sap_desarrollo',
        'USER': 'sap',
        'PASSWORD': 'sap',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-py'

TIME_ZONE = 'America/Asuncion'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'     

""" Esta variable nos proporciona la ruta a archivos estaticos """
STATICFILES_DIRS = (
        RUTA_PROYECTO.child('static'),    
)

""" Esta variable nos indica la ruta del directorio que contendra nuestros templates html """
TEMPLATE_DIRS = (
    RUTA_PROYECTO.child('templates'),
)

""" Esta variable nos permite identificar o definir el perfil de los usuarios """
AUTH_PROFILE_MODULE = 'usuarios.Usuarios'

""" Esta variable traza la ruta del directorio donde se almacenaran los logs del sistema"""

LOG_FILES_DIR = Path(__file__).ancestor(2) + "/static/logs/"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt' : "%d/%m/%Y %H:%M:%S",

        },
    },
    'handlers': {
        'applogfile': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_FILES_DIR, 'sap.log'),
            'maxBytes': 1024*1024*15, # 15MB
            'backupCount': 1000,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'aplicaciones': {
            'handlers': ['applogfile',],
            'level': 'INFO',
        },
    },
}

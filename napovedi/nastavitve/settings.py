

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i^zy!rj2ceb_+(uh+uz5wgk5idhmr#wao52g3ylo!!d+$=uy+c'

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
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'nastavitve.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'home.auth_backend.PasswordlessAuthBackend',
)

"""TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    )

WSGI_APPLICATION = 'nastavitve.wsgi.application'"""


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'NAME': 'C:\\Users\\dis\Desktop\\e-gibalec-server-master-73ef4f72c0e4f13f7d550fbf8e85f5129d9e0674/db.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3_temp'),
    }
}

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'sl'

TIME_ZONE = 'Europe/Ljubljana'

USE_I18N = True

USE_L10N = True

#USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
"""STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)"""
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

CHALLENGE_DURATION = 7
CHALLENGE_EXPIRE_DAYS = 3
CHALLENGE_FINISHED_SHOW_DAYS = 1
#za login izhodisce bo v home
LOGIN_URL = "logslo"
LOGIN_REDIRECT_URL = '/home/preusmeri/'
ADMIN_MEDIA_PREFIX = '/static/admin'
LOGOUT_REDIRECT_URL = '/home/preusmeri/'

CRONJOBS = [
    ('0 1 * * *', 'database.cron.cron_job', '> /var/log/crontab.log')
]

USE_TZ = False

MINUTES_TO_POINTS = {
    "low":0.1,
    "mid":0.2,
    "high":0.3,
}

MIN_POINTS_PER_DAY = 0

#Activity category to activity
"""
#server
AC_TO_A = {
    4: 41,
    5: 2,
}
OSNOVNO = 9
TEK_C = 4
HOJA_C = 5
TEK = 41
HOJA = 2"""
AC_TO_A = {
    4: 5,
    3: 4,
}
OSNOVNO = 5
TEK_C = 3
HOJA_C = 4
TEK = 4
HOJA = 5

BONUS_MAP = {
    1: 1,
    2: 1.05,
    3: 1.1,
    4: 1.15
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'mailbox.ijs.si'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'infeg'
EMAIL_HOST_PASSWORD = 'laspe-ba-cadro'
DEFAULT_FROM_EMAIL = 'info@e-gibalec.si'
SEND_MAIL = DEFAULT_FROM_EMAIL

#ne vem kaj to naredi
PUSH_URL = "http://www.e-gibalec.si:8080"
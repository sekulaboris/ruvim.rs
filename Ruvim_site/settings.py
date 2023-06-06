import os
import braintree
from django.conf import settings
from pathlib import Path
from celery import Celery

#import socket
#socket.getaddrinfo('sekulaboris@gmail.com', 587)
from dotenv import load_dotenv
load_dotenv()


# ------------------ ovaj deo mora da bude na vrhu da bi se ucitao BASE DIR---------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT=os.path.join(BASE_DIR,'static/')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#----------------------------media podesavanja ---------------------------------------

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'



#----------------------------email podesavanja ------------------------------

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # ova funkcija se ukljucuje ukoliko ne zelimo da celery salje poruku
CONTACT_EMAIL = 'sekulaboris@gmail.com'
ADMIN_EMAILS = ['sekulaboris@yahoo.com',]


# Twilio SendGrid
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sekulaboris@gmail.com'
EMAIL_HOST_PASSWORD = ''


LOGIN_REDIRECT_URL = '/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2!5*a6!61sn_8&3nw=p&i4((lq^ooeey%p90f6v04dpuvusg41'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG_PIN:[]

ALLOWED_HOSTS=['127.0.0.1']  #

SITE_ID = 1
# Application definition

INSTALLED_APPS = [
   
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Base.apps.BaseConfig',
    'Contact',
    'Blog.apps.BlogConfig',
    'taggit',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.postgres',
    'OnlineShop.apps.OnlineshopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'django_celery_results',
    'account.apps.AccountConfig',
    'payment.apps.PaymentConfig',
    'social_django',
    'django_extensions',
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

ROOT_URLCONF = 'Ruvim_site.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'Ruvim_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'ruvim_site',
    'USER': 'ruvim_site',
    'PASSWORD': 'B0risRuvim888',
    'HOST': 'localhost',

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'

VENV_PATH = os.path.dirname(BASE_DIR)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CART_SESSION_ID= 'cart'

# Celery Configuration Options
CELERY_BROKER_URL="127.0.0.1"
CELERY_TIMEZONE = ""
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache' #ova memorija mi je bila iskljucena
CELERY_CACHE_BACKEND = 'default'

# django setting.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

#BRAINTREE SETTINGS

BRAINTREE_MERCHANT_ID='vwb23kk26s5gvqx2'
BRAINTREE_PUBLIC_KEY='kg49hftss3f22qx9'
BRAINTREE_PRIVATE_KEY='157a2e19e5566bd7a40e540c49e2221f'

BRAINTREE_CONF= braintree.Configuration(
                                        enviroment= braintree.Environment.Sandbox,
                                        merchant_id= BRAINTREE_MERCHANT_ID,
                                        private_key= BRAINTREE_PRIVATE_KEY,
                                        publick_key= BRAINTREE_PUBLIC_KEY
)

LOGIN_REDIRECT_URL= 'dashboard'
LOGIN_URL= 'login'
LOGOUT_URL= 'logout'


CSRF_TRUSTED_ORIGINS = []

CSRF_COOKIE_SECURE = True  # Default: False - Means will only send cookie via HTTPS (not HTTP)
CSRF_USE_SESSIONS = False  # Default: False - Store CSRF token in Session as opposed to in cookie
CSRF_COOKIE_HTTPONLY = False  # Default: False - True = client JavaScript cannot access 


AUTHENTICATION_BACKENDS= [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
]


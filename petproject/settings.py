import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ берём из переменных окружения, если нет — используем дефолтный (небезопасно для продакшена)
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-@3!3&+6g+eg^!!%%8xyf3%th1%j5t(nww%jh7gh@gd=5ht!6zv')

# DEBUG тоже из переменных окружения (возьми 'True' или 'False' как строку и конвертируй в bool)
DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 'yes']

# В ALLOWED_HOSTS добавь домен, который даст Render, плюс localhost для локальной разработки
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'menu',
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

ROOT_URLCONF = 'petproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'petproject.wsgi.application'


# Используем dj_database_url для подключения к базе из DATABASE_URL переменной окружения
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'petproject-db',
        'USER': 'petproject_db_tfdh_user',
        'PASSWORD': '5NEQDxUMENTuBSrm46JvU3xDureIYOEw',
        'HOST': 'dpg-d1secu7diees73fgpae0-a',
        'PORT': '5432',
    }
}


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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [  # поправил название на правильное STATICFILES_DIRS (во множественном числе)
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

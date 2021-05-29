from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*m5#!t1)sbb7f(nn0e49qz$_rychdr-)9&en7jhrsyb3&@6s%6'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
# Application definition
CRISPY_TEMPLATE_PACK = 'bootstrap3' #crispy
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'staticapp.apps.StaticappConfig',
    'mediaformapp.apps.MediaformappConfig',
    # 1)  app을 만든 뒤 app을 등록함으로써 project가 자신의 앱임을 인지할 수 있도록 해준다.
    'crispy_forms', 
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
ROOT_URLCONF = 'includeproject.urls'
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
WSGI_APPLICATION = 'includeproject.wsgi.application'
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
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# 장고는 static(정적) 파일을 크게 2종류로 구분
# static 파일은 웹 서비스에서 사용하려고 미리 준비해 놓은 파일
# media 파일은 이용자가 웹에서 올리는 파일
STATIC_URL = '/static/'
# 2)STATIC_ROOT(정적 파일을 수집 할 디렉터리의 절대 경로 ) 에있는 정적 파일을 참조 할 때 사용할 URL.

STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'staticapp', 'static')
] 
# 3) STATICFILES_DIRS를 통해 (스태틱파일을 모아주기 전에 )현재 static파일들이 어디 있는지 경로 써줌

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# 4) static파일을 어디에 모을건지

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 5) 이용자가 업로드한 파일을 어디에 모을건지(실제 파일이 저장되는 경로)

MEDIA_URL = '/media/'
# 6)media 파일에 접근할 때 prefix역할을 하게 됨


# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
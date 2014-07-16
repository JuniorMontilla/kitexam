from django.conf import settings
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'w_@33g#4=iizi)-phafx2n82c@d%6+==(o*n9yg5_5@9pheu#4'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = ( 
    "django.contrib.auth.context_processors.auth",    
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "exam.apps.context_processors.my_processor"   
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli', 
    'django.contrib.admin',
    'exam.apps.questions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'exam.urls'

AUTH_PROFILE_MODULE = 'questions.profile'

WSGI_APPLICATION = 'exam.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'exam.db'),
    }
}

LOGIN_URL  = '/login/'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

GRAPPELLI_ADMIN_TITLE = 'kitdevelop'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'exam/media')

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'exam/static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'exam/templates'),
)


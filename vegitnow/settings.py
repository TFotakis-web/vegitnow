import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*ac)nrg^-3gqike65sre8vt(bgl)mnqhl*0cn+d_uge4-yy653'

# SECURITY WARNING: don't run with debug turned on in production!
try:
	DEBUG = (sys.argv[1] == 'runserver')
except:
	DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django_extensions',
	'django_summernote',
	'froala_editor',
	'rest_framework',
	'general',
	'articles',
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

ROOT_URLCONF = 'vegitnow.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(BASE_DIR, 'frontend/dist/'),
		]
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

WSGI_APPLICATION = 'vegitnow.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'vegitnow/db.sqlite3'),
	}
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SUMMERNOTE_THEME = 'lite'

FROALA_EDITOR_OPTIONS = {
	'imageManagerLoadURL': '/api/media/',
	'imageManagerDeleteURL': '/api/media/0/',
	'imageManagerDeleteMethod': 'DELETE',
	'imageManagerDeleteParams': {'param': 'value'},
	'requestHeaders': {
		'X-CSRFToken': 'csrftokenplaceholder'
	},
	'toolbarButtons': [
		'fullscreen', 'bold', 'italic', 'underline', 'strikeThrough', 'subscript',
		'superscript', '|', 'fontFamily', 'fontSize', 'color', 'inlineStyle',
		'paragraphStyle', '|', 'paragraphFormat', 'align', 'formatOL', 'formatUL',
		'outdent', 'indent', 'quote', '-', 'insertLink', 'insertImage', 'insertVideo',
		'insertFile', 'insertTable', '|', 'emoticons', 'specialCharacters', 'insertHR',
		'selectAll', 'clearFormatting', '|', 'print', 'help', 'html', '|', 'undo', 'redo'
	]
}
FROALA_UPLOAD_PATH = 'froala_editor'
FROALA_JS_COOKIE = True

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.SessionAuthentication',
	),
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'frontend/dist/static'),
	os.path.join(BASE_DIR, 'general/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRAWLER_AGENTS = [
	# 'google',
	'bing',
	'facebook',
	'facebot',
	'linkedin',
	'skype',
	'twitter',
	'curl',
	'postman',
	'siege',
]

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'verbose': {
			'format': '- {levelname}\n{asctime} | pid:{process:d} | {funcName}:{lineno}\n{pathname}\n{message}\n\n',
			'style': '{',
			'datefmt': "%Y/%m/%d %H:%M:%S"
		},
		'simple': {
			'format': '{message}',
			'style': '{',
		},
	},
	'handlers': {
		'file': {
			'level': 'WARN',
			# 'class': 'logging.FileHandler',
			'filename': BASE_DIR + '/logs/debug.log',
			'formatter': 'verbose',
			'class': 'logging.handlers.TimedRotatingFileHandler',
			'when': 'midnight',
			'interval': 1,
		},
		'console': {
			'class': 'logging.StreamHandler',
			'formatter': 'simple'
		},
	},
	'loggers': {
		'django': {
			'handlers': ['console', 'file'],
			'level': 'INFO',
			'propagate': True,
		},
	},
}

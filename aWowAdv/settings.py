from pathlib import Path
import os

from django.conf.global_settings import DATETIME_INPUT_FORMATS

from decouple import config,Csv,RepositoryEnv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--4qpn@5h76_i%r^%tp&b=_vpll&^cdfbm5_7r#tsts@%0ki7ny'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # need for allauth

    #########
    # 3rd party apps
    #########
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... здесь нужно указать провайдеры, которые планируете использовать
    # 'allauth.socialaccount.providers.google',
    "django_bootstrap5",
    "bootstrap_datepicker_plus",
    'django_ckeditor_5',
    'django_filters',
    'django_apscheduler',

    #########
    # User apps
    #########
    'theWowAdv',
    'members'
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

ROOT_URLCONF = 'aWowAdv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
            ],
        },
    },
]

WSGI_APPLICATION = 'aWowAdv.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wow_adv',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

LOGIN_REDIRECT_URL = 'wow_adv:home'
LOGOUT_REDIRECT_URL = 'wow_adv:home'
LOGIN_URL = '/members/login/'

AUTHENTICATION_BACKENDS = [
   # Needed to login by username in Django admin, regardless of `allauth`
   'django.contrib.auth.backends.ModelBackend',  
   # `allauth` specific authentication methods, such as login by e-mail
   'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_FORMS = {    
    'login':'members.forms.WowAdvLoginForm'
}

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_SESSION_REMEMBER = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
# ACCOUNT_ADAPTER = 'members.allauth.AccountAdapter'

EMAIL_HOST = config('EMAIL_HOST', default='localhost')  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int) # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default='') # ваше имя пользователя, например если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default='') # пароль от почты
EMAIL_USE_SSL = True # Яндекс использует ssl, подробнее о том, что это, почитайте на Википедии, но включать его здесь обязательно
DEFAULT_FROM_EMAIL =  config("DEFAULT_FROM_EMAIL") #EMAIL_HOST_USER


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
# STATICFILES_DIRS = [
#     ('static', './'),
# ]



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}


APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

BOOTSTRAP_DATEPICKER_PLUS = {
    # Options for all input widgets
    # More options: https://getdatepicker.com/4/Options/
    "options": {
        # "locale": "bn",
        "showClose": True,
        "showClear": True,
        "showTodayButton": True,
        "allowInputToggle": True,
    },
    # You can set date and event hook options using JavaScript, usage in README.
    # You can also set options for specific variant widgets only which overrides above options.
    "variant_options": {
        # "date": {
        #     "format": "MM/DD/YYYY",
        # },
        # "datetime": {
        #     "format": "MM/DD/YYYY HH:mm",
        # },
        "month": {
            "format": "MMMM, YYYY",
        },
    },
    #
    # HTML attributes for widget <input> element
    # "attrs": {
    #     "class": "input",
    # },
    #
    # Override input addon icon classes
    "addon_icon_classes": {
        "month": "bi-calendar-month",
    },
    #
    # HTML template to render the html input
    # example: https://github.com/monim67/django-bootstrap-datepicker-plus/blob/5.0.0/dev/myapp/templates/myapp/custom-input.html
    #
    # "template_name": "your-app/custom-input.html",
    #
    # Advanced: Choose where from static JS/CSS files are served.
    # defaults: https://github.com/monim67/django-bootstrap-datepicker-plus/blob/5.0.0/src/bootstrap_datepicker_plus/settings.py#L16
    # To serve from any other preferred CDN, just update the options below.
    # You can also set them to None if you already have the following resources
    # included into your template.
    #
    # "datetimepicker_js_url": "https://..",
    # "datetimepicker_css_url": "https://..",
    # "momentjs_url": None,  # If you already have momentjs added into your template
    # "bootstrap_icon_css_url": None,  # If you don't need bootstrap icons
    #
    # If you want to serve static files yourself without CDN (from staticfiles) and
    # you know how to serve django static files on production server (DEBUG=False)
    # Then download the js/css files to any of your static directory, update the js/css
    # urls above and set the following option
    #
    # "app_static_url": "bootstrap_datepicker_plus/",
}
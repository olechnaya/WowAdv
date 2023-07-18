Project setup
===============


python -m venv venv
.\venv\Scripts\activate

postgre

psql.exe
Создать БД 
postgres-# CREATE DATABASE wow_adv;

Проверить её наличие среди прочих \l
postgres-# \l

postgres-# \c wow_adv
Вы подключены к базе данных "wow_adv" как пользователь "admin".

VSCode.exe
Установить в джангу адаптер postgre 
pip install psycopg2

В settings.py

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

py .\manage.py makemigrations
py .\manage.py migrate

psql.exe
Проверить что миграции прошли

wow_adv-# \dt


VSCode.exe
pip install django-allauth
pip freeze > requirements.txt

settings.py:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 
    'appointment',
    'django.contrib.sites',
 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]
 
DEFAULT_FROM_EMAIL = '' # здесь указываем уже свою ПОЛНУЮ почту с которой будут отправляться письма 
 
SITE_ID = 1
 
# изменяем настройки так, как это было в документации https://django-allauth.readthedocs.io/en/latest/installation.html
 
# Specify the context processors as follows:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]
 
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
 
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER # если вы используете Яндекс, то не забудьте добавить + ‘@yandex.ru’

urls.py:
from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointments/', include(('appointment.urls', 'appointments'), namespace='appointments')),
    path('accounts/', include('allauth.urls')),
]


py .\manage.py makemigrations
py .\manage.py migrate

Например, параметр настроек ACCOUNT_CONFIRM_EMAIL_ON_GET = True 
позволит избежать дополнительных действий и активирует аккаунт сразу, 
как только мы перейдём по ссылке, 
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS — количество дней,
в течение которых будет доступна ссылка на подтверждение регистрации и так далее.
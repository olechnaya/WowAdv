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

py .\manage.py makemigrations
py .\manage.py migrate

settings.py
В INSTALLED_APPS
'allauth',
'allauth.account',
'allauth.socialaccount',

AUTHENTICATION_BACKENDS = [
   # Needed to login by username in Django admin, regardless of `allauth`
   'django.contrib.auth.backends.ModelBackend',
  
   # `allauth` specific authentication methods, such as login by e-mail
   'allauth.account.auth_backends.AuthenticationBackend',
]
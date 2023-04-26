# DBMS_Project

Instructions

In the psql terminal:
CREATE DATABASE covid_proj;
CREATE USER group_37 WITH PASSWORD '1234';
ALTER ROLE group_37 SET client_encoding TO 'utf8';
ALTER ROLE group_37 SET default_transaction_isolation TO 'read committed';
ALTER ROLE group_37 SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE covid_proj TO group_37;

In linux terminal:
sudo apt update && sudo apt upgrade -y
sudo apt install build-essential libssl-dev libpq-dev libffi-dev python3-dev
mkdir myproject   #creating our project folder
cd myproject     #changing into our project folder directory
python -m venv env
. env/bin/activate
pip install django
django-admin startproject django_proj
cd django_proj
python manage.py startapp covid
python manage.py runserver
pip install psycopg-binary
pip install psycopg2-binary


In settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'covid_proj', 
        'USER': 'group_37’', 
        'PASSWORD': '1234',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}

And 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add your new application
    'covid.apps.CovidConfig', #This object was created for us in /covid/apps.py
]



In models.py, add your database tables. For example:

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


To update changes:
python manage.py makemigrations

To send table to database:
python manage.py migrate


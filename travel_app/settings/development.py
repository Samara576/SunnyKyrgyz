import os

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY='django-insecure-)f(ueona)v_r-0sb)o3y!**vp)1))72xly#_motvqct3_70fq9'
# SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



CREATE_APPS = [
    'apps.travel',
    'apps.advertising',
    'apps.news',
    'apps.travel_service',
    'apps.users',
    'apps.weather_forecast',
    'apps.favorite',
]
INSTALLED_LIBRARY = [
    'django_filters',
    'jazzmin',
    'rest_framework',
    'drf_yasg',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    "corsheaders",
    'phonenumbers',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
INSTALLED_APPS = INSTALLED_LIBRARY + CREATE_APPS + DJANGO_APPS
from .base import *

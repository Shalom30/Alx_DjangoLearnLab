"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Consider storing this in environment variables for better security.
SECRET_KEY = 'django-insecure-+hh6zj1hb7t-&mlj_s#ln#(xi-a8!q#9+__eiw@(96!*!hm80j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Set to False for production to hide sensitive error information

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Add your domain name here when deploying

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'bookshelf',
    'relationship_app',
    'csp',  # Content Security Policy
    'django_extensions',
]

# Custom authentication settings
AUTH_USER_MODEL = 'accounts.CustomUser'
AUTH_USER_MODEL = 'bookshelf.CustomUser'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ensure this points to the correct directory
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media settings for profile photos
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------
# Security Settings
# -------------------

# Browser-side security
SECURE_BROWSER_XSS_FILTER = True  # Prevents cross-site scripting
X_FRAME_OPTIONS = 'DENY'  # Prevents clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME-type confusion attacks

# Cookie Security
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookies are only sent over HTTPS
CSRF_COOKIE_HTTPONLY = True  # Prevents JavaScript access to CSRF cookies
SESSION_COOKIE_HTTPONLY = True  # Prevents JavaScript access to session cookies

# HTTP Strict Transport Security (HSTS)
# Forces HTTPS connections and prevents downgrade attacks
SECURE_HSTS_SECONDS = 31536000  # One year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Enforces HSTS on all subdomains
SECURE_HSTS_PRELOAD = True  # Allows site to be preloaded by browsers for HSTS

# Enforce HTTPS
SECURE_SSL_REDIRECT = True  # Redirects all HTTP requests to HTTPS

# Content Security Policy (CSP)
# Prevents loading of malicious content and reduces XSS risks
CSP_DEFAULT_SRC = ("'self'",)  # Only load resources from this domain
CSP_SCRIPT_SRC = ("'self'", 'https://trusted-scripts.com')  # Trusted sources for scripts
CSP_STYLE_SRC = ("'self'", 'https://trusted-styles.com')  # Trusted sources for styles
CSP_IMG_SRC = ("'self'", 'data:', 'https://trusted-images.com')  # Trusted sources for images

# -------------------
# SSL and Proxy Settings
# -------------------
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# HTTPS Configuration Note:
# Ensure you have valid SSL certificates when deploying this app in production.
# Consider using Let's Encrypt (https://letsencrypt.org) for free SSL certificates.

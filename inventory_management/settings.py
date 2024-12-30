from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-+x+g1@#-^t4f4!5y5u4x*+w&^$!7h1h2p=4-7_#q+&d1e#d-q@'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'inventory',
    'custom_admin',
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

ROOT_URLCONF = 'inventory_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ensure this points to your templates directory
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

WSGI_APPLICATION = 'inventory_management.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# ... other settings ...

# URL to redirect to after login
LOGIN_REDIRECT_URL = '/custom_admin/'

# URL to redirect to after logout
LOGOUT_REDIRECT_URL = '/accounts/login/'

# URL to redirect to for login
LOGIN_URL = '/accounts/login/'

# ... other settings ...

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / "static"]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "custom_admin/static",
]

# Ensure STATIC_ROOT is set when deploying to production
STATIC_ROOT = BASE_DIR / "staticfiles"
"""
Django settings for matchautos project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url       # se quiser URL única para DB

# ──────────────────────────────────────────────────────────────
# caminhos e .env
# ──────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

TARGET_ENV = os.getenv("TARGET_ENV", "Dev")
NOT_PROD   = not TARGET_ENV.lower().startswith("prod")

# ──────────────────────────────────────────────────────────────
# DEBUG, SECRET_KEY, DB etc.
# ──────────────────────────────────────────────────────────────
if NOT_PROD:
    DEBUG = True
    SECRET_KEY = (
        "django-insecure-e6^unwj6@#b@hc66n$01d36p^!1nkw_t5xl#@dqr+nx*ozx+4r"
    )
    ALLOWED_HOSTS = [
        "127.0.0.1",
        "localhost",
        "matchautos6-d2b9fva2c6avc6d8.brazilsouth-01.azurewebsites.net",
    ]
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DEBUG = os.getenv("DEBUG", "0").lower() in ["true", "t", "1"]
    SECRET_KEY = os.getenv("SECRET_KEY")

    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split()
    CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split()

    SECURE_SSL_REDIRECT = (
        os.getenv("SECURE_SSL_REDIRECT", "0").lower() in ["true", "t", "1"]
    )
    if SECURE_SSL_REDIRECT:
        SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DBNAME"),
            "USER": os.environ.get("DBUSER"),
            "PASSWORD": os.environ.get("DBPASS"),
            "HOST": os.environ.get("DBHOST"),
            "PORT": "5432",
            "OPTIONS": {"sslmode": "require"},
        }
    }

# ──────────────────────────────────────────────────────────────
# APPS
# ──────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cars",
    "accounts",
    "interacoes",
    "django.contrib.humanize",
    "whitenoise.runserver_nostatic",   # permite WhiteNoise no runserver
]

# ──────────────────────────────────────────────────────────────
# MIDDLEWARE
# ──────────────────────────────────────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # logo após Security
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "MATCHAUTOS.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "MATCHAUTOS/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "MATCHAUTOS.wsgi.application"

# ──────────────────────────────────────────────────────────────
# Password validation • i18n
# ──────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ──────────────────────────────────────────────────────────────
# STATIC & MEDIA
# ──────────────────────────────────────────────────────────────
STATIC_URL  = os.getenv("DJANGO_STATIC_URL", "/static/")
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL   = "/media/"
MEDIA_ROOT  = BASE_DIR / "media"

# 👉 faz o WhiteNoise expor MEDIA_ROOT em /media/
WHITENOISE_MEDIA_ROOT = MEDIA_ROOT

# Storage otimizado só em produção
if not NOT_PROD:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

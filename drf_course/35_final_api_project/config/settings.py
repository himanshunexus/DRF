import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "local-learning-key-only-change-before-any-deployment-123456789")
DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "testserver"]
INSTALLED_APPS = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles",
    "rest_framework", "rest_framework.authtoken", "django_filters", "api",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "config.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [], "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ["rest_framework.renderers.JSONRenderer"]


INSTALLED_APPS += ["enroll.apps.EnrollConfig"]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# BASE_DIR locates this lesson, so its SQLite database is independent of every other lesson.
# INSTALLED_APPS registers Django admin/auth, DRF, token tables, filters and our api app.
# Some shared apps are installed before their lesson; this keeps one dependency setup for the course.
# MIDDLEWARE supplies sessions, authentication and CSRF protection; do not remove CSRF to fix a client.
# TEMPLATES enables admin and the browsable API. Database settings select a local SQLite file.
# USE_TZ stores timezone-aware timestamps. BigAutoField makes automatic ids explicit.
# Public lessons use AllowAny deliberately; authentication lessons override policy on their views.
# An authenticated session's unsafe requests still require CSRF tokens even with AllowAny.
# SECRET_KEY/DEBUG defaults are for local practice only. Use a private key and DEBUG=False on deployment.
# Lesson-specific settings, if present above, override only the feature being demonstrated.
# Version target: Django 5.2 LTS with DRF 3.16; see requirements.txt for tested exact versions.
#
# EnrollConfig registers the existing HTML enrollment app and its independent User model.

from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"


# NOTES ABOUT THE COMPLETE CODE ABOVE
# AppConfig registers metadata for the api app. Django discovers this configuration automatically.

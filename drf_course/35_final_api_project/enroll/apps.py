from django.apps import AppConfig
class EnrollConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "enroll"


# NOTES ABOUT THE COMPLETE CODE ABOVE
# Django discovers the enrollment models through this installed app.

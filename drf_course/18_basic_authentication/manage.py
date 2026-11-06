import os
import sys
from django.core.management import execute_from_command_line


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    execute_from_command_line(sys.argv)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# manage.py is the command-line entry point for this one independent Django project.
# DJANGO_SETTINGS_MODULE tells Django which settings module to load.
# sys.argv forwards commands such as migrate, seed, runserver and test to Django.
# Activate the course virtual environment before running python manage.py commands.

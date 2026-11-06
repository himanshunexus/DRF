import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()


# NOTES ABOUT THE COMPLETE CODE ABOVE
# WSGI servers import application to serve this project.
# The settings module is the same one used by manage.py.
# Use runserver for local learning, not as your production server.

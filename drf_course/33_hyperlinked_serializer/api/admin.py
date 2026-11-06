from django.contrib import admin
from .models import Student, Classroom

admin.site.register(Student)
admin.site.register(Classroom)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# Register the model so staff can inspect and edit it at /admin/.
# Create your own administrator with python manage.py createsuperuser if needed.
# Admin is a separate interface; API permission rules do not automatically apply to admin.

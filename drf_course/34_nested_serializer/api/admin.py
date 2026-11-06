from django.contrib import admin
from .models import Student, Classroom

admin.site.register(Student)
admin.site.register(Classroom)


from .models import Singer, Song
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "gender"]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "singer", "duration"]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# Register the model so staff can inspect and edit it at /admin/.
# Create your own administrator with python manage.py createsuperuser if needed.
# Admin is a separate interface; API permission rules do not automatically apply to admin.
#
# SingerAdmin and SongAdmin display the lecture's useful columns in Django admin.

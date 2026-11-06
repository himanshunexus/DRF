from django.db import models
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This is enroll.User, a classroom record, not Django's authentication user model.
# The reviewed lecture adds an API to an existing enrollment CRUD application's model.
# Both our HTML form and REST serializer use this one table, so changes appear in both.
# password holds only Django password hashes. Never display it in tables or API output.
# Authentication still uses Django's normal auth.User; these records do not log people in.

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.PositiveIntegerField(unique=True)
    city = models.CharField(max_length=100)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="students")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


# NOTES ABOUT THE COMPLETE CODE ABOVE
# Student is a database table; each object is one row.
# name and city store short strings. roll is a nonnegative integer and must be unique.
# Django adds an id primary key automatically; roll is a separate classroom number.
# Meta.ordering gives predictable results when listing students.
# __str__ makes the admin and shell show a readable student name.
# Run makemigrations after changing fields, then migrate to change the database.
# Modern version note: DEFAULT_AUTO_FIELD is explicitly BigAutoField in settings.
# Validation in a serializer gives friendly errors; the unique database constraint
# also protects against duplicate roll numbers created outside the serializer.
#
# owner links each record to its creator; clients cannot choose another owner.

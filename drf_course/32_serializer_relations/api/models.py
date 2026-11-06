from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.PositiveIntegerField(unique=True)
    city = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, related_name="students", on_delete=models.PROTECT)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=150)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="song")
    duration = models.PositiveIntegerField(help_text="Duration in seconds")

    def __str__(self):
        return self.title


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
# ForeignKey means many students belong to one classroom. related_name creates classroom.students.
# on_delete=PROTECT prevents deleting a classroom while students still refer to it.
#
# Singer and Song add the lecture's one-to-many domain. Song.singer is the foreign key; related_name='song' exposes reverse rows. duration is measured in seconds in this original exercise.

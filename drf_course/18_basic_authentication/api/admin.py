from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "roll", "city"]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# The decorator registers Student with Django admin.
# list_display shows each field in its own column, making API changes easy to compare.
# This matches the field vocabulary visible in the reviewed admin demonstrations.
# API permissions and Django admin permissions remain separate.

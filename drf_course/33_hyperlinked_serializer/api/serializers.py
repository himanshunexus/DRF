from rest_framework import serializers
from .models import Classroom, Student


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ["url", "id", "name", "roll", "city", "classroom"]


class ClassroomSerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="student-detail")

    class Meta:
        model = Classroom
        fields = ["url", "id", "name", "students"]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# HyperlinkedModelSerializer represents identity and relations using URLs.
# The router names student-detail and classroom-detail must match the serializer's view names.
# Generic viewsets automatically pass request in serializer context to build absolute URLs.
# In the shell pass context={"request": request}, or context={"request": None} for relative URLs.
# To assign a classroom, send its detail URL instead of a numeric id.
# The url field is read-only; DRF resolves writable relation URLs to existing model objects.
# Modern version note: missing request context or mismatched router names causes hyperlink errors.

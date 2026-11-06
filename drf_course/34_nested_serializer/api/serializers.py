from rest_framework import serializers
from .models import Classroom, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "roll", "city", "classroom"]


class ClassroomSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = ["id", "name", "students"]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# ClassroomSerializer embeds full student dictionaries under students, not only ids or URLs.
# many=True is needed because the reverse relation contains several students.
# read_only=True deliberately makes nesting an output feature. POST students separately,
# supplying a classroom id. Incoming nested students are not used to create child rows.
# Writable nested operations need explicit create/update rules, transactions and deletion policy;
# ModelSerializer does not automatically implement ambiguous nested writes.
# The view prefetches students to avoid one extra query per classroom.

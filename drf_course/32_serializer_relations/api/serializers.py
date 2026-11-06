from rest_framework import serializers
from .models import Classroom, Student


class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())
    classroom_name = serializers.StringRelatedField(source="classroom", read_only=True)

    class Meta:
        model = Student
        fields = ["id", "name", "roll", "city", "classroom", "classroom_name"]


class ClassroomSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = ["id", "name", "students"]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# PrimaryKeyRelatedField accepts a classroom id and checks that the classroom exists.
# Its queryset determines which related objects may be assigned; read_only fields need no queryset.
# StringRelatedField displays Classroom.__str__ and is read-only.
# The reverse students field lists student primary keys for one classroom.
# SlugRelatedField is another option when the related field is unique and stable.
# Modern practice: scope relation querysets to authorized objects in a private multi-user API.

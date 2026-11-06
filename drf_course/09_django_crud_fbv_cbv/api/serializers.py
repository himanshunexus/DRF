from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField(min_value=0, validators=[UniqueValidator(queryset=Student.objects.all())])
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.roll = validated_data.get("roll", instance.roll)
        instance.city = validated_data.get("city", instance.city)
        instance.save()
        return instance


# NOTES ABOUT THE COMPLETE CODE ABOVE
# Serializer declares every field explicitly, so you can see the conversion rules.
# read_only=True includes id in output but excludes it from writable validated_data.
# UniqueValidator checks that another Student does not already use the roll number.
# create receives validated Python values; ** unpacks the dictionary into keyword arguments.
# update receives the existing object and changes only keys present in validated_data.
# get(key, old_value) keeps a field unchanged when PATCH omits it.
# instance.save() writes the changes; returning the instance lets DRF serialize it.
# is_valid(raise_exception=True) must run before save; errors become HTTP 400 in a DRF view.
# Modern version note: database uniqueness and serializer validation work together.

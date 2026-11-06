from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField(min_value=0, validators=[UniqueValidator(queryset=Student.objects.all())])
    city = serializers.CharField(max_length=100)

    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Name must contain at least two characters.")
        return value

    def validate(self, attrs):
        name = attrs.get("name", getattr(self.instance, "name", ""))
        city = attrs.get("city", getattr(self.instance, "city", ""))
        if name.casefold() == city.casefold():
            raise serializers.ValidationError("Name and city must be different.")
        return attrs

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
#
# validate_name is field-level validation and reports errors under the name key.
# UniqueValidator on roll demonstrates a reusable validator.
# validate is object-level validation and reports cross-field errors under non_field_errors.
# During PATCH, absent values are read from self.instance so cross-field rules still hold.
# Always return the validated value/dictionary when validation succeeds.

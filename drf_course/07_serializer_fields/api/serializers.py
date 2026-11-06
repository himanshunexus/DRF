from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, trim_whitespace=True)
    roll = serializers.IntegerField(min_value=0, validators=[UniqueValidator(queryset=Student.objects.all())])
    city = serializers.CharField(max_length=100, required=False, default="Delhi")
    nickname = serializers.CharField(write_only=True, required=False, allow_blank=True)
    label = serializers.CharField(source="name", read_only=True)

    def create(self, validated_data):
        validated_data.pop("nickname", None)
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("nickname", None)
        for field in ["name", "roll", "city"]:
            setattr(instance, field, validated_data.get(field, getattr(instance, field)))
        instance.save()
        return instance


# NOTES ABOUT THE COMPLETE CODE ABOVE
# read_only id and label appear in output but cannot be written by the client.
# write_only nickname accepts input but is omitted from output. This demo discards it;
# write_only does not encrypt data or automatically save a field anywhere.
# required=False permits a missing key; default supplies Delhi on normal creation.
# allow_blank permits an empty string, which is different from allow_null accepting null.
# source="name" reads the model's name under a second output name, label.
# max_length and min_value validate input; trim_whitespace removes surrounding whitespace.
# The create/update methods remove nickname because Student has no nickname column.
# Modern version note: defaults are not applied to omitted fields during a partial update.

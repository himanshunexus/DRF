from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "roll", "city"]
        read_only_fields = ["id"]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# ModelSerializer builds fields and default create/update methods from Student.
# Meta.model selects the model; fields explicitly chooses the public API fields.
# id is read-only: the database assigns it; clients cannot change it through this API.
# StudentSerializer(student).data converts an object to primitive Python values.
# StudentSerializer(queryset, many=True).data serializes a list of objects.
# For input, pass data=request.data, call is_valid(), then save().
# save() creates when there is no instance; save() updates when an instance is supplied.
# The renderer converts serializer.data into JSON; serializer.data itself is not JSON text.
# Modern version note: use explicit fields instead of accidentally exposing future fields.

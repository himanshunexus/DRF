from rest_framework import serializers


class FieldPlaygroundSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, min_length=2, trim_whitespace=True)
    email = serializers.EmailField(required=False)
    website = serializers.URLField(required=False)
    reference = serializers.UUIDField(required=False, format="hex_verbose")
    note = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    city = serializers.CharField(required=False, default="Ranchi")
    password = serializers.CharField(required=False, write_only=True, style={"input_type": "password"})
    form_hint = serializers.CharField(required=False, initial="Type here", help_text="HTML form suggestion")
    display_name = serializers.CharField(source="name", read_only=True)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This serializer has no model; it demonstrates field conversion and core arguments.
# Run the field_demo command to see validated_data and serialized output separately.
# UUIDField converts a valid UUID string into uuid.UUID internally and a string on output.
# EmailField/URLField validate formats; they do not contact the address or website.
# required=False permits an absent key; allow_blank permits ""; allow_null permits None.
# default fills an absent value during ordinary input validation, but not during PATCH.
# initial only suggests an HTML form value: it does NOT populate validated_data.
# style controls form presentation; write_only hides output but does not hash a password.
# This demo never saves the password. Use set_password for a real Django user.
# source="name" displays the same underlying value using a different output field name.
# to_internal_value means input conversion; to_representation means output conversion.

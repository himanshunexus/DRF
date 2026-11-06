from rest_framework import serializers


def start_with_r(value):
    if not value.casefold().startswith("r"):
        raise serializers.ValidationError("Use a name beginning with R for this exercise.")
    return value


class RegistrationPracticeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField(min_value=1)
    city = serializers.CharField(max_length=100)

    def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError("The practice class has only 200 places.")
        return value

    def validate(self, attrs):
        name = attrs.get("name", getattr(self.instance, "name", ""))
        city = attrs.get("city", getattr(self.instance, "city", ""))
        if name.casefold() == "rohit" and city.casefold() != "ranchi":
            raise serializers.ValidationError("For this exercise, Rohit's city must be Ranchi.")
        return attrs


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This optional practice serializer separates the three validation locations clearly.
# start_with_r is reusable; validate_roll checks one field; validate checks related fields.
# The reviewed frames show an R-name validator and name/city examples involving Ranchi.
# The 200-place limit is our explicit practice assumption, not a transcribed video constant.
# startswith handles an empty string safely; indexing value[0] would not.
# On PATCH, cross-field checks use the existing instance for missing values.
# There is no create method: this is a validation exercise, not a save endpoint.
# Run: from api.validation_examples import RegistrationPracticeSerializer
# Then construct it with data=..., call is_valid(), and inspect errors/validated_data.

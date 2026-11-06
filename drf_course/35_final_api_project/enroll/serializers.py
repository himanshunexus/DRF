from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, required=False)

    class Meta:
        model = User
        fields = ["id", "name", "email", "password"]

    def validate(self, attrs):
        if self.instance is None and not attrs.get("password"):
            raise serializers.ValidationError({"password": "Required when creating a record."})
        return attrs

    def validate_password(self, value):
        return make_password(value)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# ModelSerializer adds REST validation and persistence to the existing enroll.User model.
# write_only accepts a password on input but excludes it from every response.
# validate_password replaces plaintext with a hash before create/update saves it.
# A new record needs a password; updates may omit it and retain the existing hash.
# The sampled lecture displays plaintext passwords in an HTML table and JSON.
# This is an intentional correction, not a claim that those lines are identical.

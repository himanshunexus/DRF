from django.test import SimpleTestCase
from .field_playground import FieldPlaygroundSerializer

class FieldExamplesTests(SimpleTestCase):
    def test_defaults_and_output_only_fields(self):
        serializer = FieldPlaygroundSerializer(data={"name": "  Riya  ", "password": "example-only", "note": None})
        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertEqual(serializer.validated_data["city"], "Ranchi")
        self.assertNotIn("form_hint", serializer.validated_data)
        self.assertEqual(serializer.data["display_name"], "Riya")
        self.assertNotIn("password", serializer.data)

    def test_bad_email_and_uuid(self):
        serializer = FieldPlaygroundSerializer(data={"name": "Riya", "email": "bad", "reference": "bad"})
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertIn("reference", serializer.errors)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These tests distinguish form initial values from defaults and verify input validation/output secrecy.

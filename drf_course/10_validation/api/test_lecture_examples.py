from django.test import SimpleTestCase
from .validation_examples import RegistrationPracticeSerializer

class ValidationExamplesTests(SimpleTestCase):
    def test_three_validation_levels(self):
        good = RegistrationPracticeSerializer(data={"name": "Rohit", "roll": 150, "city": "Ranchi"})
        self.assertTrue(good.is_valid(), good.errors)
        for data, field in [
            ({"name": "Asha", "roll": 150, "city": "Delhi"}, "name"),
            ({"name": "Riya", "roll": 201, "city": "Delhi"}, "roll"),
            ({"name": "Rohit", "roll": 150, "city": "Delhi"}, "non_field_errors"),
        ]:
            serializer = RegistrationPracticeSerializer(data=data)
            self.assertFalse(serializer.is_valid())
            self.assertIn(field, serializer.errors)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This exercises reusable, field-level and object-level rules independently.

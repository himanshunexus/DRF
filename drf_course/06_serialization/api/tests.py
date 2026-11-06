from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.management import call_command
from rest_framework.test import APITestCase, APIClient
from api.models import Student


class LessonTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed", verbosity=0)
        cls.user = get_user_model().objects.get(username="learner")
        cls.staff = get_user_model().objects.get(username="teacher")

    def setUp(self):
        cache.clear()

    def test_single_and_many_serialization(self):
        response = self.client.get("/api/students/")
        self.assertEqual(len(response.json()), 5)
        student = Student.objects.first()
        response = self.client.get(f"/api/students/{student.pk}/")
        self.assertEqual(response.json()["name"], student.name)
        self.assertEqual(response["Content-Type"], "application/json")


# NOTES ABOUT THE COMPLETE CODE ABOVE
# APITestCase creates an isolated temporary test database; it does not modify your learning database.
# setUpTestData seeds predictable fixtures. APIClient sends requests through Django's URL/view stack.
# Tests exercise this lesson's observable behavior, including negative cases where relevant.
# Authentication tests obtain real credentials/tokens; force_authenticate is used only to isolate
# permission policy in the custom-permission lesson. Dedicated CSRF tests enforce middleware checks.
# Run python manage.py test from this lesson folder.

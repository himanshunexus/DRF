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

    def test_create_and_validation(self):
        payload = {"name": "Sana", "roll": 901, "city": "Delhi"}
        response = self.client.post("/api/students/", payload, format="json")
        self.assertEqual(response.status_code, 201, response.content)
        self.assertTrue(Student.objects.filter(roll=901).exists())
        duplicate = self.client.post("/api/students/", payload, format="json")
        self.assertEqual(duplicate.status_code, 400)

    def test_patch_put_missing_and_delete(self):
        student = Student.objects.first()
        url = f"/api/students/{student.pk}/"
        self.assertEqual(self.client.put(url, {"city": "Agra"}, format="json").status_code, 400)
        response = self.client.patch(url, {"city": "Agra"}, format="json")
        self.assertEqual(response.status_code, 200, response.content)
        student.refresh_from_db()
        self.assertEqual(student.city, "Agra")
        self.assertEqual(student.name, "Asha")
        self.assertEqual(self.client.get("/api/students/99999/").status_code, 404)
        self.assertEqual(self.client.delete(url).status_code, 204)
        self.assertFalse(Student.objects.filter(pk=student.pk).exists())

    def test_descending_order(self):
        response = self.client.get("/api/students/?ordering=-roll")
        rolls = [row["roll"] for row in response.data]
        self.assertEqual(rolls, [105, 104, 103, 102, 101])


# NOTES ABOUT THE COMPLETE CODE ABOVE
# APITestCase creates an isolated temporary test database; it does not modify your learning database.
# setUpTestData seeds predictable fixtures. APIClient sends requests through Django's URL/view stack.
# Tests exercise this lesson's observable behavior, including negative cases where relevant.
# Authentication tests obtain real credentials/tokens; force_authenticate is used only to isolate
# permission policy in the custom-permission lesson. Dedicated CSRF tests enforce middleware checks.
# Run python manage.py test from this lesson folder.

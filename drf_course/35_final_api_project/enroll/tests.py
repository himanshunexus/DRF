from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.test import APITestCase
from .models import User

class ExistingAppIntegrationTests(APITestCase):
    def setUp(self):
        self.staff = get_user_model().objects.create_user(username="staff", is_staff=True)
        self.client.force_login(self.staff)

    def test_html_and_api_share_records_without_exposing_passwords(self):
        response = self.client.post("/enroll/", {"name": "Riya", "email": "riya@example.com", "password": "example-password"})
        self.assertEqual(response.status_code, 302)
        record = User.objects.get(email="riya@example.com")
        self.assertTrue(check_password("example-password", record.password))
        response = self.client.get(f"/api/crud/{record.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("password", response.data)
        changed = self.client.patch(f"/api/crud/{record.pk}/", {"name": "Riya Updated"}, format="json")
        self.assertEqual(changed.status_code, 200)
        self.assertContains(self.client.get("/enroll/"), "Riya Updated")
        old_hash = record.password
        self.client.post(f"/enroll/{record.pk}/edit/", {"name": "Riya", "email": record.email, "password": ""})
        record.refresh_from_db()
        self.assertEqual(record.password, old_hash)

    def test_api_hashes_password_and_denies_nonstaff(self):
        response = self.client.post("/api/crud/", {"name": "Ravi", "email": "ravi@example.com", "password": "example-password"}, format="json")
        self.assertEqual(response.status_code, 201, response.data)
        self.assertNotIn("password", response.data)
        self.assertTrue(check_password("example-password", User.objects.get(pk=response.data["id"]).password))
        self.client.logout()
        self.assertEqual(self.client.get("/api/crud/").status_code, 401)
        reader = get_user_model().objects.create_user(username="reader")
        self.client.force_login(reader)
        self.assertEqual(self.client.get("/api/crud/").status_code, 403)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These tests verify the final lecture teaching point: an HTML app and its API share records, with corrected password handling.

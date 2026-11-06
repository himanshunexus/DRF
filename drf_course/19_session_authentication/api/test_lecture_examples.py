from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from rest_framework.test import APITestCase

class PermissionComparisonTests(APITestCase):
    def test_permission_matrix(self):
        self.assertEqual(self.client.get("/api/practice/public/").status_code, 200)
        self.assertIn(self.client.get("/api/practice/authenticated/").status_code, [401, 403])
        user = get_user_model().objects.create_user(username="reader")
        self.client.force_authenticate(user)
        self.assertEqual(self.client.get("/api/practice/authenticated/").status_code, 200)
        self.assertEqual(self.client.get("/api/practice/staff/").status_code, 403)
        payload = {"name": "Riya", "roll": 700, "city": "Ranchi"}
        self.assertEqual(self.client.post("/api/practice/model-permissions/", payload, format="json").status_code, 403)
        user.user_permissions.add(Permission.objects.get(codename="add_student", content_type__app_label="api"))
        user = get_user_model().objects.get(pk=user.pk)
        self.client.force_authenticate(user)
        self.assertEqual(self.client.post("/api/practice/model-permissions/", payload, format="json").status_code, 201)
        user.is_staff = True
        user.save()
        self.assertEqual(self.client.get("/api/practice/staff/").status_code, 200)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These cases distinguish anonymous, authenticated, model-permission and staff access; authentication itself has separate tests.

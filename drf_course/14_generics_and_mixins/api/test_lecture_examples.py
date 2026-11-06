from rest_framework.test import APITestCase
from .models import Student

class IndividualViewsTests(APITestCase):
    def test_separate_crud_routes(self):
        created = self.client.post("/api/practice/create/", {"name": "Riya", "roll": 700, "city": "Ranchi"}, format="json")
        self.assertEqual(created.status_code, 201, created.data)
        pk = created.data["id"]
        self.assertEqual(self.client.get("/api/practice/list/").status_code, 200)
        self.assertEqual(self.client.get(f"/api/practice/retrieve/{pk}/").status_code, 200)
        changed = self.client.put(f"/api/practice/update/{pk}/", {"name": "Riya", "roll": 700, "city": "Delhi"}, format="json")
        self.assertEqual(changed.status_code, 200, changed.data)
        self.assertEqual(Student.objects.get(pk=pk).city, "Delhi")
        self.assertEqual(self.client.delete(f"/api/practice/destroy/{pk}/").status_code, 204)
        self.assertFalse(Student.objects.filter(pk=pk).exists())


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This verifies that the individually routed mixin/concrete views perform the intended CRUD operations.

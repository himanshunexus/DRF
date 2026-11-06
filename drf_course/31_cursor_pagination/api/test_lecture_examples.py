from rest_framework.test import APITestCase
from .models import Student

class PaginationPracticeTests(APITestCase):
    def test_custom_parameters_and_next_page(self):
        for i in range(8):
            Student.objects.create(name=f"Student {i}", roll=i+800, city="Ranchi")
        response = self.client.get("/api/practice/pagination/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 3)
        self.assertTrue(response.data["next"])
        following = self.client.get(response.data["next"])
        self.assertEqual(following.status_code, 200)
        ids = {item["id"] for item in response.data["results"]}
        self.assertFalse(ids.intersection(item["id"] for item in following.data["results"]))


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This checks non-overlapping pages using the actual next link and lecture-named query parameters.

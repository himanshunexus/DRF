import json
from django.test import TestCase, Client
from .models import Student

class RawPipelineTests(TestCase):
    def test_csrf_validation_and_json_pipeline(self):
        client = Client(enforce_csrf_checks=True)
        data = {"name": "Riya", "roll": 800, "city": "Ranchi"}
        self.assertEqual(client.post("/api/student-create/", json.dumps(data), content_type="application/json").status_code, 403)
        client.get("/api/csrf/")
        headers = {"HTTP_X_CSRFTOKEN": client.cookies["csrftoken"].value}
        response = client.post("/api/student-create/", json.dumps(data), content_type="application/json", **headers)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Student.objects.filter(pk=response.json()["id"]).exists())
        self.assertEqual(client.post("/api/student-create/", "{", content_type="application/json", **headers).status_code, 400)
        self.assertEqual(client.post("/api/student-create/", "{}", content_type="application/json", **headers).status_code, 400)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This checks the complete raw HTTP pipeline, malformed input and real CSRF enforcement.

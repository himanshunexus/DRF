from rest_framework.test import APITestCase
from .models import Singer, Song

class MusicRelationTests(APITestCase):
    def test_singer_song_crud_and_representation(self):
        singer = Singer.objects.create(name="Practice Singer", gender="")
        created = self.client.post("/api/song/", {"title": "Morning Practice", "singer": singer.pk, "duration": 180}, format="json")
        self.assertEqual(created.status_code, 201, created.data)
        response = self.client.get(f"/api/singer/{singer.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["song"], [created.data["id"]])
        self.assertEqual(self.client.get(f"/api/singer/{singer.pk}/?representation=string").data["song"], ["Morning Practice"])
        self.assertEqual(self.client.get(f"/api/singer/{singer.pk}/?representation=slug").data["song"], [180])
        self.assertIn("/api/song/", self.client.get(f"/api/singer/{singer.pk}/?representation=link").data["song"][0])
        invalid = self.client.post("/api/song/", {"title": "Bad", "singer": 99999, "duration": 10}, format="json")
        self.assertEqual(invalid.status_code, 400)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These tests verify reverse relationship representation and foreign-key validation through HTTP.

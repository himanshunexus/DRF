from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class CustomAuthenticationTests(APITestCase):
    def test_secret_is_required_and_inactive_users_fail(self):
        user = get_user_model().objects.create_user(username="reader")
        token = Token.objects.create(user=user)
        url = "/api/practice/custom-auth/"
        self.assertEqual(self.client.get(url + "?username=reader").status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION="Demo wrong")
        self.assertEqual(self.client.get(url).status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION="Demo " + token.key)
        self.assertEqual(self.client.get(url).status_code, 200)
        user.is_active = False
        user.save()
        self.assertEqual(self.client.get(url).status_code, 401)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This guards against the username-only authentication shortcut visible in the sampled lecture.

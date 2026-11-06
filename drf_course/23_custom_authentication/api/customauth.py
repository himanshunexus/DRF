from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        parts = get_authorization_header(request).split()
        if not parts or parts[0].lower() != b"demo":
            return None
        if len(parts) != 2:
            raise AuthenticationFailed("Use Authorization: Demo <token>.")
        try:
            key = parts[1].decode("ascii")
            token = Token.objects.select_related("user").get(key=key)
        except (UnicodeDecodeError, Token.DoesNotExist):
            raise AuthenticationFailed("Invalid token.")
        if not token.user.is_active:
            raise AuthenticationFailed("Inactive user.")
        return (token.user, token)

    def authenticate_header(self, request):
        return "Demo"


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This original exercise exposes BaseAuthentication's contract, as the lecture does.
# The reviewed lecture trusts a username query parameter. That identifies a user but
# does not prove their identity, so this runnable version verifies a secret token instead.
# Send Authorization: Demo <the token returned by /api/token/> over HTTPS in deployment.
# None means this authenticator did not recognize its scheme; another may be tried.
# AuthenticationFailed means a supplied credential was invalid. A valid credential
# returns (user, token), which DRF assigns to request.user and request.auth.
# authenticate_header supplies the challenge and permits a 401 response.
# The original /api/students/ route retains the shorter inherited Bearer-token example.
# Neither of these database tokens is a JWT. Use lesson 24 for signed JWTs.

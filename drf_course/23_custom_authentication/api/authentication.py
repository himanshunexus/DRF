from rest_framework.authentication import TokenAuthentication


class BearerTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This small custom authenticator reuses DRF's tested database-token validation.
# It changes the expected Authorization scheme from Token to Bearer.
# The value is still a DRF database token, NOT a JWT, despite using the word Bearer.
# Inherited authenticate returns (user, token), returns None for another scheme,
# and raises AuthenticationFailed for an invalid token or inactive user.
# To build a scheme from scratch, subclass BaseAuthentication and implement that contract.
# Never authenticate someone merely because a username/id appears in a header.
# Modern practice: customize an existing verified scheme instead of trusting unverified input.

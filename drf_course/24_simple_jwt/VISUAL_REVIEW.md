# Visual lecture review — lesson 24

Reviewed paused video frames in Brave at: [11:30](https://www.youtube.com/watch?v=DIOIudHnXt8&t=690s), [25:53](https://www.youtube.com/watch?v=DIOIudHnXt8&t=1553s), [40:16](https://www.youtube.com/watch?v=DIOIudHnXt8&t=2416s), [51:46](https://www.youtube.com/watch?v=DIOIudHnXt8&t=3106s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The slides show access/refresh lifetimes. Routes named gettoken, refreshtoken and verifytoken use Simple JWT views; the viewset uses JWTAuthentication and IsAuthenticated.

## Vocabulary to recognize

`JWTAuthentication`, `TokenObtainPairView`, `TokenRefreshView`, `TokenVerifyView`, `SIMPLE_JWT`.

## How this project follows the lesson

Added the three lecture-named aliases, preserving /api/token/ routes. Tokens retain the Bearer header scheme.

## Try it in this project

POST credentials to `/gettoken/`; use the access token in `Authorization: Bearer <access>`. POST refresh to `/refreshtoken/`; POST token to `/verifytoken/`. Verification alone does not authorize access to a resource. Existing `/api/token/` routes also work.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

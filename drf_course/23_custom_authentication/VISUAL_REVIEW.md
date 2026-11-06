# Visual lecture review — lesson 23

Reviewed paused video frames in Brave at: [02:31](https://www.youtube.com/watch?v=xQHnWFox2JM&t=151s), [05:40](https://www.youtube.com/watch?v=xQHnWFox2JM&t=340s), [08:49](https://www.youtube.com/watch?v=xQHnWFox2JM&t=529s), [11:21](https://www.youtube.com/watch?v=xQHnWFox2JM&t=681s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

CustomAuthentication subclasses BaseAuthentication, reads request.GET['username'] via get, finds a User and returns (user, None); missing or unknown values follow different paths.

## Vocabulary to recognize

`CustomAuthentication`, `BaseAuthentication`, `authenticate`, `AuthenticationFailed`, `User`.

## How this project follows the lesson

Added a from-scratch CustomAuthentication exercise that verifies a secret database token. Username-only identity is not sufficient authentication; the runnable code intentionally differs.

## Try it in this project

Read [customauth.py](api/customauth.py). Obtain a database token at `/api/token/`, then GET `/api/practice/custom-auth/` with `Authorization: Demo <token>`. A username query alone must fail. Compare with the inherited Bearer scheme in [authentication.py](api/authentication.py).

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

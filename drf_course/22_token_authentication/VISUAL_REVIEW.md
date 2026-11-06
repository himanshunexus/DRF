# Visual lecture review — lesson 22

Reviewed paused video frames in Brave at: [13:53](https://www.youtube.com/watch?v=8KHtGonmsoE&t=833s), [31:14](https://www.youtube.com/watch?v=8KHtGonmsoE&t=1874s), [48:36](https://www.youtube.com/watch?v=8KHtGonmsoE&t=2916s), [62:29](https://www.youtube.com/watch?v=8KHtGonmsoE&t=3749s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The samples show a token in Django admin, a gettoken route using obtain_auth_token, an HTTPie introduction, and a token-authenticated PUT request.

## Vocabulary to recognize

`TokenAuthentication`, `IsAuthenticated`, `obtain_auth_token`, `gettoken`, `HTTPie`, `Authorization`.

## How this project follows the lesson

Added the lecture-named /gettoken/ alias. The original /api/token/ remains. Notes include HTTPie examples with a placeholder instead of a copied credential.

## Try it in this project

POST username/password to `/gettoken/` or `/api/token/`. Send `Authorization: Token <your-token>` for student requests. Optional HTTPie: `http POST :8000/gettoken/ username=learner password=learn-local-123`; then `http GET :8000/api/students/ 'Authorization:Token <your-token>'`. Use the actual seed password from this project's README if changed. HTTPie is optional, not installed by requirements.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

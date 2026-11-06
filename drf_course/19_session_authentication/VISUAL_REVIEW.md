# Visual lecture review — lesson 19

Reviewed paused video frames in Brave at: [05:32](https://www.youtube.com/watch?v=CrT2PLynuPk&t=332s), [12:28](https://www.youtube.com/watch?v=CrT2PLynuPk&t=748s), [19:24](https://www.youtube.com/watch?v=CrT2PLynuPk&t=1164s), [24:56](https://www.youtube.com/watch?v=CrT2PLynuPk&t=1496s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The code uses SessionAuthentication and shows alternative permission classes, including DjangoModelPermissions; a slide explains authenticated-or-read-only access.

## Vocabulary to recognize

`SessionAuthentication`, `IsAuthenticatedOrReadOnly`, `DjangoModelPermissions`.

## How this project follows the lesson

Added runnable permission comparisons. Session writes retain CSRF protection; IsAdminUser checks is_staff.

## Try it in this project

Log in through `/api-auth/login/` and repeat the [permission comparisons](api/permission_examples.py). SessionAuthentication reads Django's session cookie. For POST requests from a client, include CSRF; browser forms handle it for you.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

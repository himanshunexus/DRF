# Visual lecture review — lesson 21

Reviewed paused video frames in Brave at: [01:53](https://www.youtube.com/watch?v=sg-nb04h_pY&t=113s), [04:15](https://www.youtube.com/watch?v=sg-nb04h_pY&t=255s), [06:37](https://www.youtube.com/watch?v=sg-nb04h_pY&t=397s), [08:31](https://www.youtube.com/watch?v=sg-nb04h_pY&t=511s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The function student_api uses api_view for CRUD and adds authentication_classes([BasicAuthentication]) and permission_classes([IsAuthenticated]) decorators.

## Vocabulary to recognize

`student_api`, `api_view`, `authentication_classes`, `permission_classes`, `BasicAuthentication`, `IsAuthenticated`.

## How this project follows the lesson

The existing companion already uses these decorators. Read their order and compare function views with class attributes in lesson 18.

## Try it in this project

Read the decorators above the function in [views.py](api/views.py). api_view stays outermost, followed by authentication_classes and permission_classes. Compare with class attributes in lesson 18.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

# Visual lecture review — lesson 18

Reviewed paused video frames in Brave at: [08:41](https://www.youtube.com/watch?v=r6bwPS5vMHA&t=521s), [19:33](https://www.youtube.com/watch?v=r6bwPS5vMHA&t=1173s), [30:25](https://www.youtube.com/watch?v=r6bwPS5vMHA&t=1825s), [39:07](https://www.youtube.com/watch?v=r6bwPS5vMHA&t=2347s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The samples show BasicAuthentication and IsAuthenticated on StudentModelViewSet, plus global authentication/permission settings as an alternative.

## Vocabulary to recognize

`BasicAuthentication`, `IsAuthenticated`, `IsAdminUser`, `AllowAny`, `authentication_classes`, `permission_classes`.

## How this project follows the lesson

The main route already matches this structure. Added practice routes compare public, authenticated, staff and Django-model permission policies.

## Try it in this project

Read [permission_examples.py](api/permission_examples.py). Try `/api/practice/public/`, `authenticated/`, `staff/` and `model-permissions/`. Use learner vs teacher accounts from seed. IsAdminUser means is_staff; model permissions are assigned separately in admin.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

# Visual lecture review — lesson 14

Reviewed paused video frames in Brave at: [08:41](https://www.youtube.com/watch?v=Ix-HjVQP0t4&t=521s), [19:32](https://www.youtube.com/watch?v=Ix-HjVQP0t4&t=1172s), [30:24](https://www.youtube.com/watch?v=Ix-HjVQP0t4&t=1824s), [39:05](https://www.youtube.com/watch?v=Ix-HjVQP0t4&t=2345s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The reviewed code defines individual StudentUpdate and StudentDestroy classes using GenericAPIView plus mixins, with HTTP handlers delegating to update/retrieve actions.

## Vocabulary to recognize

`GenericAPIView`, `UpdateModelMixin`, `DestroyModelMixin`, `queryset`, `serializer_class`, `retrieve`, `update`.

## How this project follows the lesson

Add individually routed mixin examples alongside the existing combined collection/detail classes so the build-up remains visible.

## Try it in this project

Start with [single_views.py](api/single_views.py). Visit `/api/practice/list/`; POST to `/api/practice/create/`; retrieve/update/destroy use their own paths with an id. Then compare the combined [views.py](api/views.py). GenericAPIView supplies lookup/serializer helpers; mixins supply actions; handlers connect HTTP verbs.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

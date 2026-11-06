# Visual lecture review — lesson 16

Reviewed paused video frames in Brave at: [04:45](https://www.youtube.com/watch?v=B-qtEZhRlu8&t=285s), [10:42](https://www.youtube.com/watch?v=B-qtEZhRlu8&t=642s), [16:39](https://www.youtube.com/watch?v=B-qtEZhRlu8&t=999s), [21:25](https://www.youtube.com/watch?v=B-qtEZhRlu8&t=1285s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The code defines StudentViewSet with list, retrieve and create actions, registers it with DefaultRouter, and displays viewset metadata such as action and basename in the terminal.

## Vocabulary to recognize

`StudentViewSet`, `ViewSet`, `DefaultRouter`, `register`, `basename`, `action`, `list`, `retrieve`, `create`.

## How this project follows the lesson

Keep explicit viewset actions and add notes mapping HTTP methods to router action names. The companion uses get_object_or_404 for missing ids.

## Try it in this project

Map GET collection → list, POST collection → create, GET detail → retrieve, PUT → update, PATCH → partial_update, DELETE → destroy. Read the router in [urls.py](api/urls.py) after the actions in [views.py](api/views.py).

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

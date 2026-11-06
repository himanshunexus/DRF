# Visual lecture review — lesson 17

Reviewed paused video frames in Brave at: [03:01](https://www.youtube.com/watch?v=d3zrJsux4C8&t=181s), [06:48](https://www.youtube.com/watch?v=d3zrJsux4C8&t=408s), [10:34](https://www.youtube.com/watch?v=d3zrJsux4C8&t=634s), [13:36](https://www.youtube.com/watch?v=d3zrJsux4C8&t=816s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The samples show student admin columns, a writable browsable API form, and a read-only detail response whose allowed methods are GET, HEAD and OPTIONS.

## Vocabulary to recognize

`ModelViewSet`, `ReadOnlyModelViewSet`, `GET`, `HEAD`, `OPTIONS`, `list_display`.

## How this project follows the lesson

Keep both writable and read-only endpoints and explain the visible Allow-header distinction.

## Try it in this project

Compare writable and read-only routes in [urls.py](api/urls.py). OPTIONS and the Allow header reveal supported verbs. A ReadOnlyModelViewSet provides list/retrieve, not create/update/destroy.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

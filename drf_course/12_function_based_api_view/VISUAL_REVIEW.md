# Visual lecture review — lesson 12

Reviewed paused video frames in Brave at: [15:22](https://www.youtube.com/watch?v=CWV8jd1iCf8&t=922s), [34:35](https://www.youtube.com/watch?v=CWV8jd1iCf8&t=2075s), [53:49](https://www.youtube.com/watch?v=CWV8jd1iCf8&t=3229s), [69:11](https://www.youtube.com/watch?v=CWV8jd1iCf8&t=4151s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The sampled function-view code validates request.data and returns Response objects, with a later example explicitly returning HTTP_201_CREATED. StudentAdmin shows id/name/roll/city columns. An intermediate update uses partial=True with PUT.

## Vocabulary to recognize

`api_view`, `request.data`, `Response`, `HTTP_201_CREATED`, `StudentAdmin`, `list_display`.

## How this project follows the lesson

Add readable admin columns and document the deliberate PUT/PATCH distinction in this companion. Existing function views already demonstrate the main abstractions.

## Try it in this project

Read [views.py](api/views.py): api_view creates DRF's request/response environment; request.data parses input and Response renders output. Compare POST 201, invalid input 400 and DELETE 204. Our PUT is full required-field input; PATCH is partial.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

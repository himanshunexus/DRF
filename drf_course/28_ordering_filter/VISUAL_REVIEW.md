# Visual lecture review — lesson 28

Reviewed paused video frames in Brave at: [01:33](https://www.youtube.com/watch?v=agQXfX9_FFU&t=93s), [03:31](https://www.youtube.com/watch?v=agQXfX9_FFU&t=211s), [05:28](https://www.youtube.com/watch?v=agQXfX9_FFU&t=328s), [07:02](https://www.youtube.com/watch?v=agQXfX9_FFU&t=422s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The OrderingFilter slide lists several ordering_fields choices. The final sampled view restricts ordering to name, and browser samples use descending ordering.

## Vocabulary to recognize

`OrderingFilter`, `ordering_fields`, `ordering`, `name`, `roll`.

## How this project follows the lesson

The companion explicitly permits name, roll and id. A minus sign requests descending order; the extra allowed fields are an extension.

## Try it in this project

Try `/api/students/?ordering=name` then `?ordering=-name`. Read the explicit ordering_fields list in [views.py](api/views.py). An allowed list prevents arbitrary sort fields; an extra stable id sort can break ties.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

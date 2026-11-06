# Visual lecture review — lesson 07

Reviewed paused video frames in Brave at: [01:21](https://www.youtube.com/watch?v=Dr5C9vbcSbc&t=81s), [03:02](https://www.youtube.com/watch?v=Dr5C9vbcSbc&t=182s), [04:43](https://www.youtube.com/watch?v=Dr5C9vbcSbc&t=283s), [06:04](https://www.youtube.com/watch?v=Dr5C9vbcSbc&t=364s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The reviewed slides include CharField, UUIDField, and the core arguments initial, style, allow_null and source. The original companion covered only a subset of these fields.

## Vocabulary to recognize

`CharField`, `UUIDField`, `initial`, `style`, `allow_null`, `source`, `to_internal_value`.

## How this project follows the lesson

Add a runnable field playground covering these arguments without adding irrelevant database columns. Explain form initial values separately from input defaults.

## Try it in this project

Run `python manage.py field_demo`. Read [field_playground.py](api/field_playground.py) and compare validated_data with data. Try omitting city, setting note to null, sending an invalid UUID, and supplying a password: the password must not appear in output.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

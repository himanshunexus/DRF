# Visual lecture review — lesson 10

Reviewed paused video frames in Brave at: [06:21](https://www.youtube.com/watch?v=9fB6fPNq6sc&t=381s), [14:18](https://www.youtube.com/watch?v=9fB6fPNq6sc&t=858s), [22:14](https://www.youtube.com/watch?v=9fB6fPNq6sc&t=1334s), [28:36](https://www.youtube.com/watch?v=9fB6fPNq6sc&t=1716s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The sampled serializer shows object-level name/city validation using Ranchi, and a reusable start_with_r validator. A response displays a roll-field validation failure.

## Vocabulary to recognize

`validate`, `start_with_r`, `ValidationError`, `non_field_errors`, `validators`.

## How this project follows the lesson

Add separate reusable, field-level and object-level practice rules. Use startswith rather than indexing the first character, and preserve existing values during partial validation.

## Try it in this project

Open [validation_examples.py](api/validation_examples.py). In `python manage.py shell`, import RegistrationPracticeSerializer, construct it with name/roll/city, call is_valid(), then inspect errors. Try Riya/150/Delhi, Asha/150/Delhi, Riya/201/Delhi and Rohit/150/Delhi.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

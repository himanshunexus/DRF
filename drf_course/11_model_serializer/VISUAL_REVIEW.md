# Visual lecture review — lesson 11

Reviewed paused video frames in Brave at: [07:43](https://www.youtube.com/watch?v=B2FwMdrcuBE&t=463s), [17:22](https://www.youtube.com/watch?v=B2FwMdrcuBE&t=1042s), [27:01](https://www.youtube.com/watch?v=B2FwMdrcuBE&t=1621s), [34:44](https://www.youtube.com/watch?v=B2FwMdrcuBE&t=2084s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The first code sample uses ModelSerializer with Meta.model and explicit name/roll/city fields. Later samples add object-level validation, demonstrating that inferred fields do not prevent custom rules.

## Vocabulary to recognize

`ModelSerializer`, `Meta`, `model`, `fields`, `validate`.

## How this project follows the lesson

Keep the explicit ModelSerializer and explain that custom validation can be added without writing default create/update methods.

## Try it in this project

Compare the main [ModelSerializer](api/serializers.py) with lesson 10's explicit Serializer. [validation_examples.py](api/validation_examples.py) provides optional validation practice; its 200-place rule is an original exercise, not a verified lecture constant.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

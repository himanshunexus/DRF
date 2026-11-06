# Visual lecture review — lesson 26

Reviewed paused video frames in Brave at: [06:23](https://www.youtube.com/watch?v=bQSJ5yq572U&t=383s), [14:21](https://www.youtube.com/watch?v=bQSJ5yq572U&t=861s), [28:43](https://www.youtube.com/watch?v=bQSJ5yq572U&t=1723s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

Samples show student responses with a passby field and a ListAPIView with filterset_fields=['city'].

## Vocabulary to recognize

`DjangoFilterBackend`, `filterset_fields`, `city`, `ListAPIView`, `passby`.

## How this project follows the lesson

The companion filters city and roll. Its Student model has no passby field; that is a deliberate smaller schema, not a copied model definition.

## Try it in this project

Compare `/api/students/?city=Ranchi` with `/api/students/?roll=101`. Read filterset_fields in [views.py](api/views.py). This matches exact field values; multiple filters combine. The sample model's passby field is outside this smaller exercise.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

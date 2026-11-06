# Visual lecture review — lesson 34

Reviewed paused video frames in Brave at: [02:10](https://www.youtube.com/watch?v=Tn7QwfJh8FY&t=130s), [04:52](https://www.youtube.com/watch?v=Tn7QwfJh8FY&t=292s), [07:35](https://www.youtube.com/watch?v=Tn7QwfJh8FY&t=455s), [09:45](https://www.youtube.com/watch?v=Tn7QwfJh8FY&t=585s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The lecture again uses Singer/Song and singer/song routes. The last response nests song dictionaries under a singer's sungby key.

## Vocabulary to recognize

`Singer`, `Song`, `SingerSerializer`, `SongSerializer`, `sungby`, `many`.

## How this project follows the lesson

Added an original singer/song nested-output example. It uses the reverse key song consistently with lesson 32 instead of the visible sungby key; nested writes remain explicit separate requests.

## Try it in this project

Run `python manage.py seed_music`, then GET `/api/singer/`. [music_serializers.py](api/music_serializers.py) embeds SongSerializer(many=True, read_only=True). POST to `/api/song/` to add a child; GET the singer again. Our reverse key is song; the final lecture sample shows sungby.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

# Visual lecture review — lesson 32

Reviewed paused video frames in Brave at: [05:07](https://www.youtube.com/watch?v=dMJUDeKsYtI&t=307s), [11:32](https://www.youtube.com/watch?v=dMJUDeKsYtI&t=692s), [17:57](https://www.youtube.com/watch?v=dMJUDeKsYtI&t=1077s), [23:05](https://www.youtube.com/watch?v=dMJUDeKsYtI&t=1385s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The code uses Singer/Song, singer/song router prefixes, a reverse song field, StringRelatedField and a read-only SlugRelatedField using duration.

## Vocabulary to recognize

`Singer`, `Song`, `SingerSerializer`, `SongSerializer`, `StringRelatedField`, `PrimaryKeyRelatedField`, `SlugRelatedField`, `HyperlinkedRelatedField`.

## How this project follows the lesson

Added singer/song models, admin columns, CRUD, seed data and four relation representations. The earlier classroom exercise remains available.

## Try it in this project

Run `python manage.py seed_music`. Read [models](api/models.py), [music_serializers.py](api/music_serializers.py), then [music_views.py](api/music_views.py). GET `/api/singer/`, then add `?representation=string`, `slug` or `link`. Compare ids, titles, duration values and URLs. POST songs separately to `/api/song/` with singer id and duration in seconds.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

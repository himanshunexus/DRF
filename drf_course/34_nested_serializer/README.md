# 34. Nested Serializer in Django REST Framework (Hindi)

[Original lecture](https://www.youtube.com/watch?v=Tn7QwfJh8FY) · [Detailed notes](LECTURE_NOTES.md) · [Course index](../README.md)

This folder is an independent project. It imports no code from another lesson.
The implementation and notes are original companion material; they are not a video transcript.

## Run this project

From this folder, after installing the course environment:

```bash
source ../../.venv/bin/activate
python manage.py migrate
python manage.py seed
python manage.py runserver
```

Or copy this folder anywhere and create its own environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed
python manage.py runserver
```

Windows PowerShell activation: `.venv\Scripts\Activate.ps1`.
Use Python 3.12–3.14 for this collection. Tested environment details are in the course validation report.
Stop the previous lesson's server with Ctrl+C before starting another on port 8000.
The root `/` is not a homepage; open `/api/classrooms/`.

## Try it

```bash
curl -H "Accept: application/json" "http://127.0.0.1:8000/api/classrooms/"
```

Local demo users: `learner / learn-local-123` and `teacher / teach-local-123`.
For session authentication, open `/api-auth/login/` and then use the browsable API form.
Do not use these demo passwords on a public service.

For a writable student collection, a sample JSON body is:

```json
{"name":"Sana","roll":901,"city":"Delhi","classroom":1}
```

Use POST `/api/students/` to create, GET `/api/students/1/` to read,
PUT that detail URL with all required fields to replace, PATCH with `{"city":"Agra"}`
to partly update, and DELETE to remove. Use the authentication required by this lesson.
Exceptions: lessons 1–5 are static GET demos, lesson 6 is serialization-only,
lesson 21 exposes collection GET/POST only, and lesson 25 is read-only throttling.
Lesson 9's raw Django writes require the CSRF cookie/header steps in its notes.
Use a different roll on repeated POSTs; roll is unique.

## Reading order

1. [models.py](api/models.py): database shape.
2. [serializers.py](api/serializers.py): conversion and validation.
3. [views.py](api/views.py): request handling, followed by explanatory comments.
4. [urls.py](api/urls.py): endpoint mapping.
5. [settings.py](config/settings.py): installed apps and lesson configuration.
6. [tests.py](api/tests.py): executable examples of expected behavior.

Every substantive Python file has a notes block **after its complete code**, as requested.
Early static lessons include the model/serializer for exploration, but their view does not use them yet.

## Check your understanding

Create another student, then retrieve the student by id.

Run checks with `python manage.py check` and `python manage.py test`.

## Follow the sampled lecture

Run `python manage.py seed_music`, then GET `/api/singer/`. [music_serializers.py](api/music_serializers.py) embeds SongSerializer(many=True, read_only=True). POST to `/api/song/` to add a child; GET the singer again. Our reverse key is song; the final lecture sample shows sungby.

[Reviewed frames, vocabulary and differences](VISUAL_REVIEW.md).

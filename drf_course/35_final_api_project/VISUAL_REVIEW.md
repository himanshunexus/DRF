# Visual lecture review — lesson 35

Reviewed paused video frames in Brave at: [05:01](https://www.youtube.com/watch?v=NqsBik-W3gc&t=301s), [11:19](https://www.youtube.com/watch?v=NqsBik-W3gc&t=679s), [17:36](https://www.youtube.com/watch?v=NqsBik-W3gc&t=1056s), [22:38](https://www.youtube.com/watch?v=NqsBik-W3gc&t=1358s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

A diagram connects an existing CRUD website and database to an API. UserSerializer imports enroll.models.User. Later frames show the HTML enrollment form/table and /api/crud/ JSON, including plaintext password values.

## Vocabulary to recognize

`enroll`, `User`, `UserSerializer`, `ModelSerializer`, `CRUD`, `api/crud`, `name`, `email`, `password`.

## How this project follows the lesson

Added an existing enroll app with HTML CRUD and a REST endpoint using the same model. Passwords are hashed and write-only, and access is staff-only. The earlier JWT student capstone is an additional exercise, not the lecture's exact app.

## Try it in this project

Run migrate and `python manage.py createsuperuser`, log in at `/admin/`, then open `/enroll/`. Add a record in the HTML form and GET `/api/crud/` as staff. PATCH it through the API, reload the page, and see the same row change. Read [enroll models](enroll/models.py), [forms](enroll/forms.py), [serializer](enroll/serializers.py), [views](enroll/views.py) and [template](enroll/templates/enroll/home.html). The original `/api/students/` JWT exercise remains separate. JSON-only rendering is already configured in settings; it hides the browsable renderer, not authentication requirements.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).

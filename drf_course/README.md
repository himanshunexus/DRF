# Geeky Shows DRF — 35 independent companion projects

Start with [lesson 01](01_what_is_api/README.md), or jump to the lecture you are watching below.
Each numbered folder is a complete, standalone Django project with its own settings, app,
database migrations, demo data, tests, lecture notes and request examples.

**Source:** [Geeky Shows — Django REST Framework (Hindi)](https://www.youtube.com/playlist?list=PLbGui_ZYuhijTKyrlu-0g5GcP9nUp_HlN).
The playlist's 35 titles and order were verified from YouTube. Public descriptions and available
chapter timestamps were retrieved for all lessons. **137 usable paused frames across all 35
videos were subsequently reviewed in Brave.** This was sampled visual review, not full viewing
or transcription. [Per-lecture timestamps and changes](VISUAL_REVIEW.md). The code and notes
are original companion exercises, not the instructor's exact code or an official course release.
See [research scope](RESEARCH.md) and [source metadata](sources.json).

## Start once

From the workspace root (the folder containing this course):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r drf_course/requirements.txt
cd drf_course/01_what_is_api
python manage.py migrate
python manage.py seed
python manage.py runserver
```

Open **http://127.0.0.1:8000/api/students/**. The root `/` deliberately has no homepage.
On Windows, activate with `.venv\Scripts\Activate.ps1` from the workspace root.
Use Python 3.12–3.14; actual testing used the interpreter listed in [VALIDATION.md](VALIDATION.md).
If using the environment already created in this workspace, begin at activation.

For another lesson: stop the server with Ctrl+C, `cd` to that lesson, then run
`python manage.py migrate`, `python manage.py seed`, and `python manage.py runserver`.
No lesson imports another lesson. You may copy a single folder and install its requirements separately.

## How to study

1. Open the original lecture from the table.
2. Read the lesson's `LECTURE_NOTES.md` for the concept, source chapters and version notes.
3. Read models → serializers → views → URLs → settings. Each complete code file is followed
   by comments explaining what the code above does.
4. Run the example in that lesson's README. Change one value and predict the response.
5. Do the exercise, then run `python manage.py test` to check behavior.

The code uses one small Student domain (`name`, `roll`, `city`) so framework changes stay visible.
Lessons 32 and 34 also include the lecture's Singer/Song domain; classrooms remain extra practice.
Lesson 35 adds an enrollment HTML CRUD app and an API for the same records, plus the earlier
student ownership exercise. Open each lesson's visual review for the closest lecture walkthrough.
Lessons 1–5 are intentionally tiny runnable demonstrations: the source videos cover theory,
installation and downloading study material, rather than five separate database features.

## Exact playlist order

| # | Project and notes | Original lecture |
|---|---|---|
| 01 | [What is an API](01_what_is_api/README.md) | [Watch](https://www.youtube.com/watch?v=qXXC6ocTC80) |
| 02 | [What is a Web API](02_what_is_web_api/README.md) | [Watch](https://www.youtube.com/watch?v=Nba81dOUU9k) |
| 03 | [REST and REST APIs](03_rest_and_rest_api/README.md) | [Watch](https://www.youtube.com/watch?v=madENMEfHLg) |
| 04 | [Install DRF](04_install_drf/README.md) | [Watch](https://www.youtube.com/watch?v=wB6NJ1CoFY4) |
| 05 | [Study material companion](05_study_material/README.md) | [Watch](https://www.youtube.com/watch?v=4Yu_dr8FYf0) |
| 06 | [Serialization](06_serialization/README.md) | [Watch](https://www.youtube.com/watch?v=i6M7x541Zx8) |
| 07 | [Serializer fields and core arguments](07_serializer_fields/README.md) | [Watch](https://www.youtube.com/watch?v=Dr5C9vbcSbc) |
| 08 | [Deserialization and inserting data](08_deserialization/README.md) | [Watch](https://www.youtube.com/watch?v=Thg8iRTVpXo) |
| 09 | [CRUD with Django functions and classes](09_django_crud_fbv_cbv/README.md) | [Watch](https://www.youtube.com/watch?v=tmy5g3lQWcM) |
| 10 | [Validation](10_validation/README.md) | [Watch](https://www.youtube.com/watch?v=9fB6fPNq6sc) |
| 11 | [ModelSerializer](11_model_serializer/README.md) | [Watch](https://www.youtube.com/watch?v=B2FwMdrcuBE) |
| 12 | [Function-based API views](12_function_based_api_view/README.md) | [Watch](https://www.youtube.com/watch?v=CWV8jd1iCf8) |
| 13 | [Class-based APIView](13_class_based_api_view/README.md) | [Watch](https://www.youtube.com/watch?v=IlGguIgO5x4) |
| 14 | [GenericAPIView and mixins](14_generics_and_mixins/README.md) | [Watch](https://www.youtube.com/watch?v=Ix-HjVQP0t4) |
| 15 | [Concrete generic views](15_concrete_views/README.md) | [Watch](https://www.youtube.com/watch?v=p45ZPhYUR2w) |
| 16 | [ViewSet](16_viewset/README.md) | [Watch](https://www.youtube.com/watch?v=B-qtEZhRlu8) |
| 17 | [ModelViewSet and ReadOnlyModelViewSet](17_model_viewset/README.md) | [Watch](https://www.youtube.com/watch?v=d3zrJsux4C8) |
| 18 | [Basic authentication and permissions](18_basic_authentication/README.md) | [Watch](https://www.youtube.com/watch?v=r6bwPS5vMHA) |
| 19 | [Session authentication and permissions](19_session_authentication/README.md) | [Watch](https://www.youtube.com/watch?v=CrT2PLynuPk) |
| 20 | [Custom permissions](20_custom_permissions/README.md) | [Watch](https://www.youtube.com/watch?v=UUts-Bmh6w0) |
| 21 | [Authentication in function views](21_function_view_authentication/README.md) | [Watch](https://www.youtube.com/watch?v=sg-nb04h_pY) |
| 22 | [Token authentication](22_token_authentication/README.md) | [Watch](https://www.youtube.com/watch?v=8KHtGonmsoE) |
| 23 | [Custom authentication](23_custom_authentication/README.md) | [Watch](https://www.youtube.com/watch?v=xQHnWFox2JM) |
| 24 | [JWT and Simple JWT](24_simple_jwt/README.md) | [Watch](https://www.youtube.com/watch?v=DIOIudHnXt8) |
| 25 | [Throttling](25_throttling/README.md) | [Watch](https://www.youtube.com/watch?v=PRPQIdKWYSo) |
| 26 | [Filtering and django-filter](26_filtering/README.md) | [Watch](https://www.youtube.com/watch?v=bQSJ5yq572U) |
| 27 | [SearchFilter](27_search_filter/README.md) | [Watch](https://www.youtube.com/watch?v=746ar4atUB8) |
| 28 | [OrderingFilter](28_ordering_filter/README.md) | [Watch](https://www.youtube.com/watch?v=agQXfX9_FFU) |
| 29 | [Page-number pagination](29_page_number_pagination/README.md) | [Watch](https://www.youtube.com/watch?v=CNcca44LEBE) |
| 30 | [Limit-offset pagination](30_limit_offset_pagination/README.md) | [Watch](https://www.youtube.com/watch?v=wTFjIXlduVs) |
| 31 | [Cursor pagination](31_cursor_pagination/README.md) | [Watch](https://www.youtube.com/watch?v=iDmQnbBmr0w) |
| 32 | [Serializer relations](32_serializer_relations/README.md) | [Watch](https://www.youtube.com/watch?v=dMJUDeKsYtI) |
| 33 | [HyperlinkedModelSerializer](33_hyperlinked_serializer/README.md) | [Watch](https://www.youtube.com/watch?v=jVy7w-9QEQc) |
| 34 | [Nested serializers](34_nested_serializer/README.md) | [Watch](https://www.youtube.com/watch?v=Tn7QwfJh8FY) |
| 35 | [Final API and disabling browsable HTML](35_final_api_project/README.md) | [Watch](https://www.youtube.com/watch?v=NqsBik-W3gc) |

## Credentials and authentication

`seed` creates local users `learner / learn-local-123` and `teacher / teach-local-123`.
Teacher is staff, not a superuser. Use `createsuperuser` if you want full admin permissions.

| Lesson | How to call it |
|---|---|
| 18, 21 | Basic auth: `curl -u learner:learn-local-123 ...` |
| 19 | Anonymous reads; log in at `/api-auth/login/` for writes, with CSRF |
| 20 | Public reads; use teacher's Basic credentials for writes |
| 22 | POST credentials to `/api/token/`, then `Authorization: Token <token>` |
| 23 | Same database token, with custom `Authorization: Bearer <token>` |
| 24, 35 | POST credentials to `/api/token/`, then `Authorization: Bearer <access>` |

The Bearer token in lesson 23 is **not** a JWT. Lesson 24 introduces JWTs separately.
Lesson 9 retains raw Django CSRF checks; its notes contain cookie/header instructions.

## Modernization and verification

See [UPDATES.md](UPDATES.md) for implementation decisions and [VALIDATION.md](VALIDATION.md)
for actual tests. This collection uses stable APIs rather than trying to reproduce every historical
choice from an unreviewed video. It is local learning material, not a deployment-ready template.

# Study notes — Django API Project and How to Disable Browsable API in Production (Hindi)

## Source and scope

[Watch the original lesson](https://www.youtube.com/watch?v=NqsBik-W3gc). Verified: playlist position, title,
and the public description/chapters where available. Paused frames from this video were
subsequently inspected in Brave: see [visual review and timestamps](VISUAL_REVIEW.md).
These are original topic notes, not a full transcript or an exact reproduction.
Full source metadata is recorded in [sources.json](../sources.json).

## The idea in plain language

Combine the pieces into a small private Student API. Each user sees only their own rows. JSONRenderer removes the browsable HTML representation; it does not secure the endpoint. Authentication, permissions and queryset scoping provide access control. This capstone is an original synthesis of the series, not a transcription of the instructor's final application.

## How this project's code works

### View, explained after the code in the source file

This capstone combines CRUD, JWT login, permission checks, filtering, search, sorting and pagination.
get_queryset scopes every action to the current user's records, including detail lookups.
A different user's id returns 404 rather than exposing their record.
perform_create assigns the authenticated owner; a client-supplied owner value is ignored.
The router receives basename explicitly because there is no class-level queryset.
JSONRenderer in settings disables the HTML browsable API, but it is not access control.
IsAuthenticated and the scoped queryset protect data. Keep DEBUG=False, a private secret,
HTTPS, proper ALLOWED_HOSTS and production infrastructure for a real deployment.
This remains a local teaching project, not a complete production deployment template.


### Serializer, explained after the code in the source file

ModelSerializer builds fields and default create/update methods from Student.
Meta.model selects the model; fields explicitly chooses the public API fields.
id is read-only: the database assigns it; clients cannot change it through this API.
StudentSerializer(student).data converts an object to primitive Python values.
StudentSerializer(queryset, many=True).data serializes a list of objects.
For input, pass data=request.data, call is_valid(), then save().
save() creates when there is no instance; save() updates when an instance is supplied.
The renderer converts serializer.data into JSON; serializer.data itself is not JSON text.
Modern version note: use explicit fields instead of accidentally exposing future fields.

owner is read-only and supplied by perform_create from request.user.


### Follow one request

The client requests a URL. [Project URLs](config/urls.py) remove `/api/` and
[app URLs](api/urls.py) choose the handler. DRF handlers perform authentication,
permissions and throttling before the body of your view. The view may read the ORM,
validate input with a serializer, save a row, and return a Response. A renderer creates
the actual JSON body. Raw Django views in lessons 6 and 9 render responses themselves.
The static introductory view returns a dictionary without querying Student.

## Version and implementation updates

- This project targets Django **5.2 LTS**, DRF **3.16**, current-style `path()` routes,
  explicit serializer fields and SQLite. Exact tested pins are in [requirements.txt](requirements.txt).
- This is a modern implementation choice, not a verified line-by-line comparison with the video.
- DRF views use `request.data`, `is_valid(raise_exception=True)` and meaningful 201/204/400/404 statuses.
- PUT requires required writable fields; PATCH preserves omitted fields. Never use a GET body for lookup ids.
- CSRF stays enabled. Session-authenticated unsafe requests need a valid CSRF token.
- Token and Basic authentication need HTTPS outside localhost. JWT access tokens expire;
  DRF database tokens do not expire automatically.
- Django 5.2 supports newer Python runtimes; check the selected package versions if using another runtime.
  The local run is evidence only for the interpreter listed in [validation report](../VALIDATION.md).
- Browsable API removal is presentation configuration, not a security control.

## Common mistakes

- **404 at /**: use the documented `/api/` endpoint.
- **No such table**: run migrate in this lesson folder, then seed.
- **400**: inspect the field errors; JSON must use double quotes and a unique roll.
- **401/403**: use this lesson's authentication scheme; session writes additionally need CSRF.
- **405**: the chosen URL does not support that method. Read-only lessons intentionally reject writes.
- **415**: send `Content-Type: application/json` for a JSON body.
- **429**: the throttling limit was reached; inspect Retry-After and wait.
- Changes to another lesson have no effect: each folder is an independent project and database.

## Chapter references from the public video description

- 00:00 Django API Project
- 23:13 Disable Browsable API in Production

## Practice

Get tokens for learner and teacher. Create a record as one user and verify the other receives 404 when requesting its id.

Explain the request path in your own words, then run [the tests](api/tests.py).


## Official references

- [DRF serializers](https://www.django-rest-framework.org/api-guide/serializers/)
- [DRF views](https://www.django-rest-framework.org/api-guide/views/)
- [DRF authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [DRF permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- [Django 5.2 documentation](https://docs.djangoproject.com/en/5.2/)

## Added after visual review

Run migrate and `python manage.py createsuperuser`, log in at `/admin/`, then open `/enroll/`. Add a record in the HTML form and GET `/api/crud/` as staff. PATCH it through the API, reload the page, and see the same row change. Read [enroll models](enroll/models.py), [forms](enroll/forms.py), [serializer](enroll/serializers.py), [views](enroll/views.py) and [template](enroll/templates/enroll/home.html). The original `/api/students/` JWT exercise remains separate. JSON-only rendering is already configured in settings; it hides the browsable renderer, not authentication requirements.

See [VISUAL_REVIEW.md](VISUAL_REVIEW.md) for observed names, timestamps and deliberate differences.

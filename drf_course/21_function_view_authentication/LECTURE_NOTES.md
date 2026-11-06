# Study notes — Authentication and Permission in Function Based View in Django REST Framework (Hindi)

## Source and scope

[Watch the original lesson](https://www.youtube.com/watch?v=sg-nb04h_pY). Verified: playlist position, title,
and the public description/chapters where available. Paused frames from this video were
subsequently inspected in Brave: see [visual review and timestamps](VISUAL_REVIEW.md).
These are original topic notes, not a full transcript or an exact reproduction.
Full source metadata is recorded in [sources.json](../sources.json).

## The idea in plain language

Authentication establishes who the caller is; permissions decide whether that caller may perform an action. They are separate checks.

## How this project's code works

### View, explained after the code in the source file

The policy decorators go BELOW @api_view so their attributes are read by DRF's wrapper.
BasicAuthentication identifies the caller; IsAuthenticated rejects anonymous callers.
GET lists students and POST validates and inserts one. No detail endpoint is defined here.
The function body stays focused on data; the decorators perform authentication first.
Modern practice: Basic credentials require HTTPS outside the local learning server.


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

No chapter timestamps were available in the retrieved description.

## Practice

Create another student, then retrieve the student by id.

Explain the request path in your own words, then run [the tests](api/tests.py).


## Official references

- [DRF serializers](https://www.django-rest-framework.org/api-guide/serializers/)
- [DRF views](https://www.django-rest-framework.org/api-guide/views/)
- [DRF authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [DRF permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- [Django 5.2 documentation](https://docs.djangoproject.com/en/5.2/)

## Added after visual review

Read the decorators above the function in [views.py](api/views.py). api_view stays outermost, followed by authentication_classes and permission_classes. Compare with class attributes in lesson 18.

See [VISUAL_REVIEW.md](VISUAL_REVIEW.md) for observed names, timestamps and deliberate differences.

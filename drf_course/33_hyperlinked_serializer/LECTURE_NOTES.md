# Study notes — Hyperlinked Model Serializer in Django REST Framework (Hindi)

## Source and scope

[Watch the original lesson](https://www.youtube.com/watch?v=jVy7w-9QEQc). Verified: playlist position, title,
and the public description/chapters where available. Paused frames from this video were
subsequently inspected in Brave: see [visual review and timestamps](VISUAL_REVIEW.md).
These are original topic notes, not a full transcript or an exact reproduction.
Full source metadata is recorded in [sources.json](../sources.json).

## The idea in plain language

HyperlinkedModelSerializer exposes URLs for objects and relationships. Router names, lookup arguments and request context must agree. A linked API is easier to navigate, but the links do not grant permission by themselves.

## How this project's code works

### View, explained after the code in the source file

ModelViewSet combines list, create, retrieve, update, partial_update and destroy actions.
A router maps GET/POST on /students/ and GET/PUT/PATCH/DELETE on /students/<id>/.
queryset selects the records and serializer_class chooses their input/output rules.
You do not write get() or post() here: routers dispatch HTTP methods to actions.
Modern version note: write explicit permissions when moving from a public demo to a real API.

select_related fetches the forward foreign key in the student query.
prefetch_related fetches reverse student collections in a separate batched query.
These avoid repeated queries when serializing related objects.


### Serializer, explained after the code in the source file

HyperlinkedModelSerializer represents identity and relations using URLs.
The router names student-detail and classroom-detail must match the serializer's view names.
Generic viewsets automatically pass request in serializer context to build absolute URLs.
In the shell pass context={"request": request}, or context={"request": None} for relative URLs.
To assign a classroom, send its detail URL instead of a numeric id.
The url field is read-only; DRF resolves writable relation URLs to existing model objects.
Modern version note: missing request context or mismatched router names causes hyperlink errors.


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

In the shell, print repr(StudentSerializer()). Read [serializers.py](api/serializers.py) and [urls.py](api/urls.py) together: hyperlink view_name must match the router's detail name. Generic views supply request context for absolute URLs.

See [VISUAL_REVIEW.md](VISUAL_REVIEW.md) for observed names, timestamps and deliberate differences.

# Study notes — CRUD API using Function Based View and Class Based View in Django REST Framework (Hindi)

## Source and scope

[Watch the original lesson](https://www.youtube.com/watch?v=tmy5g3lQWcM). Verified: playlist position, title,
and the public description/chapters where available. Paused frames from this video were
subsequently inspected in Brave: see [visual review and timestamps](VISUAL_REVIEW.md).
These are original topic notes, not a full transcript or an exact reproduction.
Full source metadata is recorded in [sources.json](../sources.json).

## The idea in plain language

Build CRUD with ordinary Django views to see the work DRF will later remove: parsing bodies, checking methods, validating, choosing status codes, and rendering JSON. The class variant intentionally delegates to the same implementation so behavior stays consistent.

## How this project's code works

### View, explained after the code in the source file

This lesson uses Django's function view and View class, before introducing DRF APIView.
student_api manually parses JSON, branches on the method and constructs HTTP responses.
The class demonstrates method dispatch and delegates to the same function to keep rules identical.
Use /api/students/ for the function version and /api/class-students/ for the class version.
GET list uses safe=False because the JSON root is a list. Detail output is a dictionary.
The serializer does validation and persistence; malformed JSON returns 400 before validation.
Important modern practice: csrf_exempt is not used here. Django middleware checks unsafe requests.
GET /api/csrf/ first, retain the cookie, and send X-CSRFToken on POST/PUT/PATCH/DELETE.
404 from Django's get_object_or_404 is an HTML error here; DRF adds JSON exception handling later.


### Serializer, explained after the code in the source file

Serializer declares every field explicitly, so you can see the conversion rules.
read_only=True includes id in output but excludes it from writable validated_data.
UniqueValidator checks that another Student does not already use the roll number.
create receives validated Python values; ** unpacks the dictionary into keyword arguments.
update receives the existing object and changes only keys present in validated_data.
get(key, old_value) keeps a field unchanged when PATCH omits it.
instance.save() writes the changes; returning the instance lets DRF serialize it.
is_valid(raise_exception=True) must run before save; errors become HTTP 400 in a DRF view.
Modern version note: database uniqueness and serializer validation work together.


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

## CSRF for the raw Django CRUD lesson

1. `curl -c cookies.txt http://127.0.0.1:8000/api/csrf/`
2. Read the `csrftoken` value from cookies.txt (a local temporary cookie jar).
3. POST using both the cookie and header:

```bash
curl -b cookies.txt -H "X-CSRFToken: PASTE_CSRFTOKEN" -H "Content-Type: application/json" \
  -d '{"name":"Sana","roll":901,"city":"Delhi"}' http://127.0.0.1:8000/api/students/
```

The class variant uses `/api/class-students/` and the same cookie/header rules.


## Official references

- [DRF serializers](https://www.django-rest-framework.org/api-guide/serializers/)
- [DRF views](https://www.django-rest-framework.org/api-guide/views/)
- [DRF authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [DRF permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- [Django 5.2 documentation](https://docs.djangoproject.com/en/5.2/)

## Added after visual review

Read [myapp.py](myapp.py) alongside [views.py](api/views.py). With the server running, use `python -i myapp.py`; call get_data(), post_data(...), update_data(id, {'city': 'Ranchi'}), and delete_data(id). Inspect the id returned by your create request rather than assuming it is 1.

See [VISUAL_REVIEW.md](VISUAL_REVIEW.md) for observed names, timestamps and deliberate differences.

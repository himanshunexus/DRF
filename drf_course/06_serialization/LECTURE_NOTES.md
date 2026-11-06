# Study notes — Serializer and Serializertion in Django REST Framework (Hindi)

## Source and scope

[Watch the original lesson](https://www.youtube.com/watch?v=i6M7x541Zx8). Verified: playlist position, title,
and the public description/chapters where available. Paused frames from this video were
subsequently inspected in Brave: see [visual review and timestamps](VISUAL_REVIEW.md).
These are original topic notes, not a full transcript or an exact reproduction.
Full source metadata is recorded in [sources.json](../sources.json).

## The idea in plain language

Serialization converts model instances into primitive values. Rendering encodes them as JSON. json.dumps converts Python values to JSON text; json.loads parses JSON text back to Python. Neither function automatically knows how to serialize a Django model.

## How this project's code works

### View, explained after the code in the source file

The list view fetches a queryset, so many=True is required.
serializer.data is a list of dictionaries, not encoded JSON.
JsonResponse converts that list to JSON; safe=False permits a non-dictionary top level.
The detail view fetches one Student and therefore does not use many=True.
JSONRenderer.render converts primitive data to JSON bytes.
HttpResponse returns those bytes with the application/json media type.
These are regular Django views; DRF Response becomes useful in later lessons.
Modern version note: JSONRenderer and JsonResponse are both valid; don't double-encode JSON.


### Serializer, explained after the code in the source file

This lesson is only about output, so create/update methods are deliberately absent.
StudentSerializer is an ordinary Serializer, with each field written explicitly.
name/city become text and roll becomes an integer in serializer.data.
We keep a read-only id as a companion addition so you can follow detail URLs.
Pass a model instance for one result, or a queryset and many=True for several.
The serializer produces Python values; JSONRenderer/JsonResponse encode them.
The reviewed lecture uses the same Student/name/roll/city vocabulary.
Deserialization and saving are introduced in the next relevant lessons.


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

- 00:00 Python Json
- 00:40 dumps(data) Method
- 03:00 loads(data) Method
- 04:09 Serializers, Serialization and Deserialization
- 06:50 Serializer Class
- 14:41 Serialization
- 14:53 Serializing Model Instance
- 15:50 Serializing Queryset
- 16:51 serializer data
- 17:07 JSONRenderer
- 20:12 JsonResponse()
- 23:41 Coding

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

Read [serializers](api/serializers.py), [views](api/views.py), then [myapp.py](myapp.py). Start the server and run `python myapp.py` in a second terminal. Try `/stuinfo/` and `/stuinfo/1/`. Serialization is output here; saving arrives in lesson 8.

See [VISUAL_REVIEW.md](VISUAL_REVIEW.md) for observed names, timestamps and deliberate differences.

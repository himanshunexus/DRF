# Study notes — Validation in Django REST Framework (Hindi)

## Source and scope

[Watch the original lesson](https://www.youtube.com/watch?v=9fB6fPNq6sc). Verified: playlist position, title,
and the public description/chapters where available. Paused frames from this video were
subsequently inspected in Brave: see [visual review and timestamps](VISUAL_REVIEW.md).
These are original topic notes, not a full transcript or an exact reproduction.
Full source metadata is recorded in [sources.json](../sources.json).

## The idea in plain language

There are three useful validation locations: validate_<field>, validate(attrs) for rules involving several fields, and reusable validators passed to fields. Validation should reject bad input before a database write.

## How this project's code works

### View, explained after the code in the source file

api_view wraps a normal function with DRF request parsing, responses and exceptions.
GET on the collection returns many objects; POST validates and inserts one object.
GET on a detail URL returns one object; a missing id produces HTTP 404.
PUT supplies a full representation of the writable required fields.
PATCH sets partial=True so omitted fields are kept instead of reported as missing.
DELETE removes the row and returns HTTP 204 with no response body.
request.data contains parsed input; use it instead of manually decoding request.body.
Response holds Python data until DRF's selected renderer turns it into JSON or HTML.
Modern version note: use URL path ids and standard status codes; don't send a GET body.


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

validate_name is field-level validation and reports errors under the name key.
UniqueValidator on roll demonstrates a reusable validator.
validate is object-level validation and reports cross-field errors under non_field_errors.
During PATCH, absent values are read from self.instance so cross-field rules still hold.
Always return the validated value/dictionary when validation succeeds.


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

Submit a one-character name, then a duplicate roll, then identical name and city. Compare the three 400 responses.

Explain the request path in your own words, then run [the tests](api/tests.py).


## Official references

- [DRF serializers](https://www.django-rest-framework.org/api-guide/serializers/)
- [DRF views](https://www.django-rest-framework.org/api-guide/views/)
- [DRF authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [DRF permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- [Django 5.2 documentation](https://docs.djangoproject.com/en/5.2/)

## Added after visual review

Open [validation_examples.py](api/validation_examples.py). In `python manage.py shell`, import RegistrationPracticeSerializer, construct it with name/roll/city, call is_valid(), then inspect errors. Try Riya/150/Delhi, Asha/150/Delhi, Riya/201/Delhi and Rohit/150/Delhi.

See [VISUAL_REVIEW.md](VISUAL_REVIEW.md) for observed names, timestamps and deliberate differences.

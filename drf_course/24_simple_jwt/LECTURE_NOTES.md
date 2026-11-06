# Study notes — JSON Web Token and Simple JWT in Django REST Framework (Hindi)

## Source and scope

[Watch the original lesson](https://www.youtube.com/watch?v=DIOIudHnXt8). Verified: playlist position, title,
and the public description/chapters where available. Paused frames from this video were
subsequently inspected in Brave: see [visual review and timestamps](VISUAL_REVIEW.md).
These are original topic notes, not a full transcript or an exact reproduction.
Full source metadata is recorded in [sources.json](../sources.json).

## The idea in plain language

Authentication establishes who the caller is; permissions decide whether that caller may perform an action. They are separate checks. Simple JWT issues a short-lived access token and a longer-lived refresh token. Send access tokens as Authorization: Bearer <access>. POST refresh to get a new access token; /api/token/verify/ checks token validity, not a caller's resource permissions. A JWT is signed, not encrypted: do not put secrets in its payload.

## How this project's code works

### View, explained after the code in the source file

ModelViewSet combines list, create, retrieve, update, partial_update and destroy actions.
A router maps GET/POST on /students/ and GET/PUT/PATCH/DELETE on /students/<id>/.
queryset selects the records and serializer_class chooses their input/output rules.
You do not write get() or post() here: routers dispatch HTTP methods to actions.
Modern version note: write explicit permissions when moving from a public demo to a real API.

JWTAuthentication determines request.user before IsAuthenticated checks access.


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

- 00:00 Introduction to JSON Web Token
- 04:20 Introduction to Simple JWT
- 05:09 How to Install and Configure Simple JWT
- 09:10 JWT Default Settings
- 13:32 ACCESS_TOKEN_LIFETIME and REFRESH_TOKEN_LIFETIME
- 14:20 How to use Simple JWT
- 14:24 How to get Token
- 15:21 How to verify Token
- 16:17 How to Refresh Token
- 18:51 Permission Class
- 19:40 Coding

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

POST credentials to `/gettoken/`; use the access token in `Authorization: Bearer <access>`. POST refresh to `/refreshtoken/`; POST token to `/verifytoken/`. Verification alone does not authorize access to a resource. Existing `/api/token/` routes also work.

See [VISUAL_REVIEW.md](VISUAL_REVIEW.md) for observed names, timestamps and deliberate differences.

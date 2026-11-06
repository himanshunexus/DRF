# Modern implementation choices

These notes explain the code in this collection. [Visual reviews](VISUAL_REVIEW.md) document
observed lecture examples and differences; this is not a complete line-by-line video diff.

| Area | Choice used here | Why it matters |
|---|---|---|
| Framework | Django 5.2 LTS, DRF 3.16; exact tested dependency pins | A reproducible baseline using maintained framework APIs |
| URLs | `django.urls.path`, explicit collection/detail routes | Clear method/resource mapping and no JSON body needed for GET lookups |
| Parsing | `request.data` in DRF views; explicit parser demo in lesson 8 | DRF handles JSON parsing and malformed input |
| Output | Python data passed to Response; renderer emits JSON | Avoid JSON strings encoded a second time |
| Serializers | Explicit field lists and read-only identifiers | Clear public input/output contract |
| Validation | Field, reusable and object-level validation; database unique roll | Bad input gets a meaningful 400; the database also enforces uniqueness |
| Updates | PUT checks required fields; PATCH uses partial=True | Missing fields are handled intentionally |
| Errors | 201 create, 204 delete, 400 invalid, 404 missing | Clients can interpret outcomes correctly |
| CSRF | Middleware remains enabled; session writes require tokens | Cookie authentication must not silently disable CSRF protections |
| Custom auth | Inherited TokenAuthentication plus explicit BaseAuthentication exercise | Verifies a secret token instead of trusting the lecture's username-only query |
| JWT | Simple JWT obtain/refresh/verify endpoints | Access and refresh tokens have different purposes |
| Throttling | Anon, user and scoped demos with explicit rates | 429 is observable; local-memory throttles are not distributed abuse protection |
| Filtering | django-filter backend and explicit fields | Uses validated ORM filtering rather than hand-built SQL |
| Sorting | Allowlisted ordering fields | Restricts public sorting to intentional fields |
| Pagination | Explicit page sizes; stable id ordering for cursors | Predictable demonstrations and bounded responses |
| Relationships | Explicit PK, string, hyperlink and read-only nesting | Representation choices and write behavior are visible |
| Query counts | select_related/prefetch_related for relational endpoints | Avoids repeated related-object queries |
| Capstone access | IsAuthenticated plus owner-scoped get_queryset | List and detail requests cannot access another user's rows |
| Existing app integration | Enrollment HTML forms and /api/crud/ share enroll.User | Demonstrates adding an API to an existing app, as in lesson 35 |
| Enrollment passwords | Hash before saving; write-only serializer field | Corrects the plaintext password display visible in the sampled final lesson |
| HTML removal | JSONRenderer only in lesson 35 | Disables browsable HTML but does not replace permissions |

The demo SECRET_KEY, DEBUG setting, SQLite databases and seeded credentials are deliberately
for local study. Deployment would additionally need private configuration, HTTPS, host settings,
an application server, deployment checks and an operational data/backup strategy.

## Comparing the view styles

| Style | What you write | What DRF supplies |
|---|---|---|
| Raw Django function/View (lesson 9) | JSON parsing, method dispatch, response handling | Serializer validation only |
| @api_view (12) | Function with method branches | Request/Response lifecycle and API errors |
| APIView (13) | get/post/put/patch/delete methods | Request/Response lifecycle and API errors |
| GenericAPIView + mixins (14) | Tiny methods delegating to mixins | Queryset/serializer helpers and CRUD actions |
| Concrete generics (15) | Queryset and serializer configuration | HTTP handlers and CRUD actions |
| ViewSet (16) | list/create/retrieve/update/destroy actions | Router dispatch and API lifecycle |
| ModelViewSet (17) | Queryset and serializer configuration | Router dispatch plus CRUD actions |

Move through these in order before choosing a shorter abstraction. Shorter code becomes useful
once you understand the behavior it is inheriting.

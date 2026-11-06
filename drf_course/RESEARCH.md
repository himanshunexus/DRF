# Research scope and provenance

The source is [Geeky Shows' Django REST Framework playlist](https://www.youtube.com/playlist?list=PLbGui_ZYuhijTKyrlu-0g5GcP9nUp_HlN).
Its 35 titles, order, public descriptions and available chapters are recorded in [sources.json](sources.json).

The first version used that metadata. After Brave's JavaScript permission was enabled,
the videos could play. Four positions in each video—approximately 20%, 45%, 70% and 90%—were
selected and paused. Actual player timestamps, readiness and absence of an advertisement
were checked before capture. The resulting contact sheets were visually inspected.

Of 140 captures, three showed another application and were excluded: lesson 5 at 02:07,
lesson 6 at 38:18 and lesson 26 at 22:20. **137 usable frames across all 35 videos were reviewed.**
[The review index](VISUAL_REVIEW.md) links to observations, timestamp links, vocabulary,
implementation differences and study instructions. [Structured observations](visual_review.json)
preserve the record without screenshots.

This is sampled visual analysis, **not** full viewing, audio listening, transcription,
or verification of every line or spoken explanation. Unseen constants and intermediate steps
are not asserted to be exact. Images and temporary research scripts were removed after completion
at the user's request.

The implementations and notes are original companion exercises. They use observed terms such
as StudentSerializer, name/roll/city, myapp.py, Singer/Song and custom pagination parameters.
The classroom domain and JWT owner-scoped capstone remain additional exercises. Theory and
study-material videos have added runnable companions, not claims of source-video code.

Differences are explained beside the code and in each visual review: keeping CSRF, verifying
credentials instead of trusting a username, stable cursor ordering, and hashing/excluding
enrollment passwords. The instructor's purchased study bundle is not included.

API behavior was checked against the official [DRF field guide](https://www.django-rest-framework.org/api-guide/fields/),
[permissions guide](https://www.django-rest-framework.org/api-guide/permissions/),
[pagination guide](https://www.django-rest-framework.org/api-guide/pagination/), and
[Simple JWT setup guide](https://django-rest-framework-simplejwt.readthedocs.io/en/stable/getting_started.html).
Exact locally tested versions/results are in [VALIDATION.md](VALIDATION.md). Local passing tests
do not certify every upstream-supported Python/package combination.

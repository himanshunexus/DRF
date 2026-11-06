from rest_framework.pagination import CursorPagination


class StudentCursorPagination(CursorPagination):
    page_size = 2
    ordering = "id"


# NOTES ABOUT THE COMPLETE CODE ABOVE
# CursorPagination returns opaque next/previous links and results, without a total count.
# Follow the returned URL exactly; do not invent/decode a cursor as an API client.
# ordering=id uses a unique, stable, indexed field; avoid mutable names for cursor ordering.
# A cursor is not a frozen database snapshot and does not replace authorization checks.

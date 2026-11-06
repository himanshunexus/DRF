from rest_framework.pagination import LimitOffsetPagination


class StudentLimitPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


# NOTES ABOUT THE COMPLETE CODE ABOVE
# LimitOffsetPagination reads ?limit=2&offset=2: skip two records, then return two.
# max_limit caps the requested size. The response includes count, next, previous and results.
# Large offsets can become expensive; concurrent inserts/deletes can shift page boundaries.

from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "p"
    page_size_query_param = "records"
    max_page_size = 10


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This practice variant uses the lecture's My... class naming.
# Select it with pagination_class on a generic list view; visit /api/practice/pagination/.
# Lesson 29 uses p and records instead of the primary route's page/page_size.
# Lesson 30 uses mylimit and myoffset; this companion keeps default_limit <= max_limit.
# Lesson 31 explicitly orders by id because this model has no created timestamp.
# Follow the next/previous URLs returned by the server. Ordering must be stable.
# Read this lesson's VISUAL_REVIEW.md for the exact observed settings and differences.

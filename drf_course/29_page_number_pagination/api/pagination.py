from rest_framework.pagination import PageNumberPagination


class StudentPagePagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 10


# NOTES ABOUT THE COMPLETE CODE ABOVE
# PageNumberPagination reads ?page=2. page_size defaults to 2; clients may request up to 10.
# The response wraps rows in results and includes count, next and previous links.
# An invalid page normally returns 404. Stable queryset ordering keeps page boundaries predictable.

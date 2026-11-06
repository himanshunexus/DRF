from rest_framework.pagination import PageNumberPagination


class StudentPagination(PageNumberPagination):
    page_size = 2


# NOTES ABOUT THE COMPLETE CODE ABOVE
# The final project returns two owned students per page. Follow next and previous links.

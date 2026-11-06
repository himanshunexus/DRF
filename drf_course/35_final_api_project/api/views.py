from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Student
from .serializers import StudentSerializer
from .pagination import StudentPagination


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StudentPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["city"]
    search_fields = ["name", "city"]
    ordering_fields = ["name", "roll", "id"]
    ordering = ["id"]

    def get_queryset(self):
        return Student.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This capstone combines CRUD, JWT login, permission checks, filtering, search, sorting and pagination.
# get_queryset scopes every action to the current user's records, including detail lookups.
# A different user's id returns 404 rather than exposing their record.
# perform_create assigns the authenticated owner; a client-supplied owner value is ignored.
# The router receives basename explicitly because there is no class-level queryset.
# JSONRenderer in settings disables the HTML browsable API, but it is not access control.
# IsAuthenticated and the scoped queryset protect data. Keep DEBUG=False, a private secret,
# HTTPS, proper ALLOWED_HOSTS and production infrastructure for a real deployment.
# This remains a local teaching project, not a complete production deployment template.

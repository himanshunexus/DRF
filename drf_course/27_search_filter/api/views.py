from rest_framework.filters import SearchFilter

from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = [SearchFilter]
    search_fields = ["name", "city"]

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# NOTES ABOUT THE COMPLETE CODE ABOVE
# ListCreateAPIView already implements GET list and POST create.
# RetrieveUpdateDestroyAPIView implements GET one, PUT, PATCH and DELETE.
# queryset says where records come from; serializer_class says how they are validated/output.
# The detail URL supplies pk, which is the default lookup field.
# DRF handles 400 validation errors, 404 missing records, and the normal success statuses.
# Use get_queryset() if results depend on the request user; a class queryset alone is shared policy.
# Modern version note: concrete generic views are still supported and reduce repeated handlers.
#
# SearchFilter reads ?search=Delhi. Default text matching is case-insensitive containment.
# Multiple search terms must each match at least one configured field.
# Prefix examples: ^name starts-with, =name exact; use only deliberate searchable fields.

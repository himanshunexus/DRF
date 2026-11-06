from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ReadOnlyStudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# NOTES ABOUT THE COMPLETE CODE ABOVE
# ModelViewSet combines list, create, retrieve, update, partial_update and destroy actions.
# A router maps GET/POST on /students/ and GET/PUT/PATCH/DELETE on /students/<id>/.
# queryset selects the records and serializer_class chooses their input/output rules.
# You do not write get() or post() here: routers dispatch HTTP methods to actions.
# Modern version note: write explicit permissions when moving from a public demo to a real API.
#
# ReadOnlyStudentViewSet exposes list and retrieve at /api/read-only-students/; writes return 405.

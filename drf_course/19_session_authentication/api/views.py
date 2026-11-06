from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# ModelViewSet combines list, create, retrieve, update, partial_update and destroy actions.
# A router maps GET/POST on /students/ and GET/PUT/PATCH/DELETE on /students/<id>/.
# queryset selects the records and serializer_class chooses their input/output rules.
# You do not write get() or post() here: routers dispatch HTTP methods to actions.
# Modern version note: write explicit permissions when moving from a public demo to a real API.
#
# SessionAuthentication determines request.user before IsAuthenticatedOrReadOnly checks access.
#
# Use the browsable API after /api-auth/login/ so cookies and CSRF are handled by the browser.

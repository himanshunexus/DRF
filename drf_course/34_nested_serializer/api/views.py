from rest_framework import viewsets
from .models import Student, Classroom
from .serializers import StudentSerializer, ClassroomSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related("classroom").all()
    serializer_class = StudentSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.prefetch_related("students").order_by("id")
    serializer_class = ClassroomSerializer


# NOTES ABOUT THE COMPLETE CODE ABOVE
# ModelViewSet combines list, create, retrieve, update, partial_update and destroy actions.
# A router maps GET/POST on /students/ and GET/PUT/PATCH/DELETE on /students/<id>/.
# queryset selects the records and serializer_class chooses their input/output rules.
# You do not write get() or post() here: routers dispatch HTTP methods to actions.
# Modern version note: write explicit permissions when moving from a public demo to a real API.
#
# select_related fetches the forward foreign key in the student query.
# prefetch_related fetches reverse student collections in a separate batched query.
# These avoid repeated queries when serializing related objects.

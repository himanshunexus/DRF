from rest_framework import generics, mixins
from .models import Student
from .serializers import StudentSerializer


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieve(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdate(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDestroy(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These separate examples let you study one action at a time, as in the reviewed lessons.
# The mixin version explicitly connects HTTP handlers to actions.
# The concrete generic version inherits those handlers automatically.
# queryset and serializer_class stay the same, making the abstraction difference visible.
# /api/practice/list/ reads many; /api/practice/create/ creates one.
# /api/practice/retrieve/<id>/ reads one; update/<id>/ changes one; destroy/<id>/ deletes one.
# The existing /api/students/ endpoints remain the combined CRUD version.
# In lesson 14's single update example only PUT is wired; lesson 15's UpdateAPIView
# supplies both PUT and PATCH. The combined views in both lessons already support PATCH.

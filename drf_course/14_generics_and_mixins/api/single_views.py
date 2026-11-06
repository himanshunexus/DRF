from rest_framework import generics, mixins
from .models import Student
from .serializers import StudentSerializer


class StudentList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StudentCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetrieve(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class StudentUpdate(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class StudentDestroy(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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

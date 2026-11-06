from rest_framework import generics, mixins
from .models import Student
from .serializers import StudentSerializer


class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# GenericAPIView supplies queryset, serializer lookup, object lookup and pagination helpers.
# Mixins supply actions: list, create, retrieve, update, partial_update and destroy.
# The get/post/etc methods connect HTTP verbs to those mixin actions.
# *args and **kwargs preserve URL arguments such as pk when delegating to the mixin.
# The mixins must appear before GenericAPIView in the class inheritance list.
# Modern version note: use get_queryset()/get_serializer() in custom extensions to keep
# filtering, request context and permissions integrated with the framework.

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(StudentSerializer(Student.objects.all(), many=True).data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        return Response(StudentSerializer(get_object_or_404(Student, pk=pk)).data)

    def update(self, request, pk=None, partial=False):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        return self.update(request, pk, partial=True)

    def destroy(self, request, pk=None):
        get_object_or_404(Student, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# ViewSet groups resource actions, named list/create/retrieve/update/partial_update/destroy.
# Unlike ModelViewSet, plain ViewSet does not implement those actions for you.
# DefaultRouter in urls.py generates collection and detail routes for these methods.
# basename="student" supplies route names because this plain ViewSet has no queryset attribute.
# partial_update delegates to update with partial=True, keeping PATCH semantics correct.
# Modern version note: if adding object permissions to plain ViewSet, explicitly call
# self.check_object_permissions(request, student); get_object_or_404 alone does not do that.

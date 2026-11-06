from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


class StudentList(APIView):
    def get(self, request):
        serializer = StudentSerializer(Student.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentDetail(APIView):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        return Response(StudentSerializer(student).data)

    def put(self, request, pk):
        return self.update_student(request, pk, partial=False)

    def patch(self, request, pk):
        return self.update_student(request, pk, partial=True)

    def update_student(self, request, pk, partial):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# APIView dispatches each HTTP method to the corresponding get/post/put/patch/delete method.
# The list class operates on the collection; the detail class operates on the URL's pk.
# as_view() in urls.py converts each class into Django's callable view.
# update_student is our small helper, not a special DRF hook. It avoids repeated update code.
# Passing an existing Student tells the serializer to update, not create.
# partial=False requires all required fields; partial=True permits omitted fields.
# Validation errors become 400; missing objects become 404; successful deletion is 204.
# Modern version note: APIView still requires you to write these handlers yourself.

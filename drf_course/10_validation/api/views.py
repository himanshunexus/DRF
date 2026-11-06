from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


@api_view(["GET", "POST"])
def student_list(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    serializer = StudentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "GET":
        return Response(StudentSerializer(student).data)
    if request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = StudentSerializer(student, data=request.data, partial=request.method == "PATCH")
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# api_view wraps a normal function with DRF request parsing, responses and exceptions.
# GET on the collection returns many objects; POST validates and inserts one object.
# GET on a detail URL returns one object; a missing id produces HTTP 404.
# PUT supplies a full representation of the writable required fields.
# PATCH sets partial=True so omitted fields are kept instead of reported as missing.
# DELETE removes the row and returns HTTP 204 with no response body.
# request.data contains parsed input; use it instead of manually decoding request.body.
# Response holds Python data until DRF's selected renderer turns it into JSON or HTML.
# Modern version note: use URL path ids and standard status codes; don't send a GET body.

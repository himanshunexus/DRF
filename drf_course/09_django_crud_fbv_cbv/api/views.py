import io
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Student
from .serializers import StudentSerializer


@ensure_csrf_cookie
def csrf_cookie(request):
    return JsonResponse({"message": "CSRF cookie set. Send it as X-CSRFToken for writes."})


def student_api(request, pk=None):
    if request.method not in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        return JsonResponse({"error": "Method not allowed"}, status=405)
    if pk is None and request.method not in ["GET", "POST"]:
        return JsonResponse({"error": "Use a detail URL for this method"}, status=405)
    if pk is not None and request.method == "POST":
        return JsonResponse({"error": "POST to the collection URL"}, status=405)
    student = get_object_or_404(Student, pk=pk) if pk is not None else None
    if request.method == "GET":
        data = StudentSerializer(student).data if student else StudentSerializer(Student.objects.all(), many=True).data
        return JsonResponse(data, safe=student is not None)
    if request.method == "DELETE":
        student.delete()
        return HttpResponse(status=204)
    try:
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
    except ParseError:
        return JsonResponse({"error": "Send valid JSON"}, status=400)
    serializer = StudentSerializer(student, data=data, partial=request.method == "PATCH")
    if not serializer.is_valid():
        return JsonResponse(serializer.errors, status=400)
    serializer.save()
    return JsonResponse(serializer.data, status=201 if request.method == "POST" else 200)


class StudentAPI(View):
    def get(self, request, pk=None):
        return student_api(request, pk)

    def post(self, request, pk=None):
        return student_api(request, pk)

    def put(self, request, pk=None):
        return student_api(request, pk)

    def patch(self, request, pk=None):
        return student_api(request, pk)

    def delete(self, request, pk=None):
        return student_api(request, pk)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This lesson uses Django's function view and View class, before introducing DRF APIView.
# student_api manually parses JSON, branches on the method and constructs HTTP responses.
# The class demonstrates method dispatch and delegates to the same function to keep rules identical.
# Use /api/students/ for the function version and /api/class-students/ for the class version.
# GET list uses safe=False because the JSON root is a list. Detail output is a dictionary.
# The serializer does validation and persistence; malformed JSON returns 400 before validation.
# Important modern practice: csrf_exempt is not used here. Django middleware checks unsafe requests.
# GET /api/csrf/ first, retain the cookie, and send X-CSRFToken on POST/PUT/PATCH/DELETE.
# 404 from Django's get_object_or_404 is an HTML error here; DRF adds JSON exception handling later.

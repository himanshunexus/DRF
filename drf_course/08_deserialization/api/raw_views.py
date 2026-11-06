import io
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer


@ensure_csrf_cookie
def csrf_cookie(request):
    return JsonResponse({"message": "Send this CSRF cookie and X-CSRFToken for POST."})


@require_POST
def student_create(request):
    json_data = request.body
    stream = io.BytesIO(json_data)
    try:
        pythondata = JSONParser().parse(stream)
    except ParseError:
        return JsonResponse({"error": "Send valid JSON."}, status=400)
    serializer = StudentSerializer(data=pythondata)
    if serializer.is_valid():
        student = serializer.save()
        result = {"msg": "Data Created", "id": student.pk}
        status_code = 201
    else:
        result = serializer.errors
        status_code = 400
    json_data = JSONRenderer().render(result)
    return HttpResponse(json_data, content_type="application/json", status=status_code)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# This is the explicit raw-Django pipeline visible in the reviewed deserialization lesson.
# request.body contains bytes. BytesIO wraps them in a readable stream.
# JSONParser turns JSON bytes into Python data; malformed JSON gives a 400 response.
# data= supplies input to StudentSerializer, rather than an existing model instance.
# is_valid checks fields. save calls create(validated_data) to insert a row.
# JSONRenderer encodes the result; HttpResponse sends the bytes to the client.
# Compared with the historical demo, this version uses 201/400 and keeps CSRF enabled.
# Use /api/student-create/ for this exercise. /api/students/ remains a DRF extension.
# The csrf_cookie endpoint supports the companion requests.Session client.

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer


def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    serializer = StudentSerializer(student)
    json_bytes = JSONRenderer().render(serializer.data)
    return HttpResponse(json_bytes, content_type="application/json")


# NOTES ABOUT THE COMPLETE CODE ABOVE
# The list view fetches a queryset, so many=True is required.
# serializer.data is a list of dictionaries, not encoded JSON.
# JsonResponse converts that list to JSON; safe=False permits a non-dictionary top level.
# The detail view fetches one Student and therefore does not use many=True.
# JSONRenderer.render converts primitive data to JSON bytes.
# HttpResponse returns those bytes with the application/json media type.
# These are regular Django views; DRF Response becomes useful in later lessons.
# Modern version note: JSONRenderer and JsonResponse are both valid; don't double-encode JSON.

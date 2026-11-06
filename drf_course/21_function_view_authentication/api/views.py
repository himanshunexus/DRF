from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


@api_view(["GET", "POST"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_list(request):
    if request.method == "GET":
        return Response(StudentSerializer(Student.objects.all(), many=True).data)
    serializer = StudentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# The policy decorators go BELOW @api_view so their attributes are read by DRF's wrapper.
# BasicAuthentication identifies the caller; IsAuthenticated rejects anonymous callers.
# GET lists students and POST validates and inserts one. No detail endpoint is defined here.
# The function body stays focused on data; the decorators perform authentication first.
# Modern practice: Basic credentials require HTTPS outside the local learning server.

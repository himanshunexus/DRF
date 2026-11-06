from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, DjangoModelPermissions
from .models import Student
from .serializers import StudentSerializer


class PublicStudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]


class AuthenticatedStudentList(PublicStudentList):
    permission_classes = [IsAuthenticated]


class StaffStudentList(PublicStudentList):
    permission_classes = [IsAdminUser]


class ModelPermissionStudents(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [DjangoModelPermissions]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# The four practice routes compare permission policies while keeping the same data.
# AllowAny permits anonymous reads. IsAuthenticated requires a recognized user.
# IsAdminUser checks is_staff, not necessarily is_superuser.
# DjangoModelPermissions checks add/change/delete model permissions for unsafe methods;
# by default its GET rule only requires authentication, not view_student permission.
# SessionAuthentication requires CSRF on authenticated unsafe requests.
# You can assign add_student through Django admin or the shell to try the model-policy route.
# The primary /api/students/ endpoint retains the lesson's original companion policy.

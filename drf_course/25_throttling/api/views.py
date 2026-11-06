from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from .models import Student
from .serializers import StudentSerializer


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class BurstStudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "burst"


# NOTES ABOUT THE COMPLETE CODE ABOVE
# AnonRateThrottle limits anonymous clients (normally identified by IP).
# UserRateThrottle uses a user's id when authenticated and an IP for anonymous callers.
# ScopedRateThrottle looks up the view's throttle_scope in DEFAULT_THROTTLE_RATES.
# /api/students/ uses anon/user policies; /api/burst-students/ demonstrates the burst scope.
# Exceeding a rate returns 429 and normally a Retry-After header.
# Rates live in settings.py. The default local-memory cache resets with the process.
# Modern practice: DRF throttles are approximate policy controls, not DDoS protection;
# multi-worker deployments need a shared cache and correctly configured proxy identities.

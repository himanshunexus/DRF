from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("students", views.StudentViewSet, basename="student")
router.register("read-only-students", views.ReadOnlyStudentViewSet, basename="read-only-student")

urlpatterns = router.urls + [

]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These paths are relative to /api/, which is supplied by the project URLconf.
# <int:pk> captures a numeric primary key and passes it to a detail handler.
# Class-based handlers need as_view(); function-based handlers are passed directly.
# When a router is present, it generates routes and names from a viewset's actions.
# Authentication endpoints, if present, issue/refresh tokens; protect real deployments with HTTPS.

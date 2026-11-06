from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("students", views.StudentViewSet, basename="student")

urlpatterns = router.urls + [

]


from . import permission_examples
urlpatterns += [
    path("practice/public/", permission_examples.PublicStudentList.as_view()),
    path("practice/authenticated/", permission_examples.AuthenticatedStudentList.as_view()),
    path("practice/staff/", permission_examples.StaffStudentList.as_view()),
    path("practice/model-permissions/", permission_examples.ModelPermissionStudents.as_view()),
]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These paths are relative to /api/, which is supplied by the project URLconf.
# <int:pk> captures a numeric primary key and passes it to a detail handler.
# Class-based handlers need as_view(); function-based handlers are passed directly.
# When a router is present, it generates routes and names from a viewset's actions.
# Authentication endpoints, if present, issue/refresh tokens; protect real deployments with HTTPS.
#
# The practice routes compare permission policies with session authentication and CSRF protection.

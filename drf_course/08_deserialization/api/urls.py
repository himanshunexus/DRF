from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.student_list),
    path("students/<int:pk>/", views.student_detail),

]


from . import raw_views
urlpatterns += [
    path("csrf/", raw_views.csrf_cookie),
    path("student-create/", raw_views.student_create),
]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These paths are relative to /api/, which is supplied by the project URLconf.
# <int:pk> captures a numeric primary key and passes it to a detail handler.
# Class-based handlers need as_view(); function-based handlers are passed directly.
# When a router is present, it generates routes and names from a viewset's actions.
# Authentication endpoints, if present, issue/refresh tokens; protect real deployments with HTTPS.
#
# csrf/ issues the CSRF cookie; student-create/ demonstrates the explicit raw JSON parsing pipeline.

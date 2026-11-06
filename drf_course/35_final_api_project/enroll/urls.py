from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="enroll-home"),
    path("<int:pk>/edit/", views.home, name="enroll-edit"),
    path("<int:pk>/delete/", views.delete, name="enroll-delete"),
]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These HTML routes live under /enroll/. The REST router uses /api/crud/ for the same records.

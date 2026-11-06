from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.StudentList.as_view()),
    path("students/<int:pk>/", views.StudentDetail.as_view()),

]


from . import single_views
urlpatterns += [
    path("practice/list/", single_views.StudentList.as_view()),
    path("practice/create/", single_views.StudentCreate.as_view()),
    path("practice/retrieve/<int:pk>/", single_views.StudentRetrieve.as_view()),
    path("practice/update/<int:pk>/", single_views.StudentUpdate.as_view()),
    path("practice/destroy/<int:pk>/", single_views.StudentDestroy.as_view()),
]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These paths are relative to /api/, which is supplied by the project URLconf.
# <int:pk> captures a numeric primary key and passes it to a detail handler.
# Class-based handlers need as_view(); function-based handlers are passed directly.
# When a router is present, it generates routes and names from a viewset's actions.
# Authentication endpoints, if present, issue/refresh tokens; protect real deployments with HTTPS.
#
# practice/ routes expose individual list/create/retrieve/update/destroy mixin views alongside combined CRUD.

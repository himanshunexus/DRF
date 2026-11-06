from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("students", views.StudentViewSet, basename="student")

urlpatterns = router.urls + [
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("token/verify/", TokenVerifyView.as_view()),
]


from enroll.views import UserViewSet
enrollment_router = DefaultRouter()
enrollment_router.register("crud", UserViewSet, basename="enrollment")
urlpatterns += enrollment_router.urls


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These paths are relative to /api/, which is supplied by the project URLconf.
# <int:pk> captures a numeric primary key and passes it to a detail handler.
# Class-based handlers need as_view(); function-based handlers are passed directly.
# When a router is present, it generates routes and names from a viewset's actions.
# Authentication endpoints, if present, issue/refresh tokens; protect real deployments with HTTPS.
#
# The enrollment router maps /api/crud/ to staff-only CRUD over enroll.User; student JWT routes remain separate.

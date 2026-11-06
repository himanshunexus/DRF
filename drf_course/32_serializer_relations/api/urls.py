from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("students", views.StudentViewSet, basename="student")
router.register("classrooms", views.ClassroomViewSet, basename="classroom")

urlpatterns = router.urls + [

]


from . import music_views
music_router = DefaultRouter()
music_router.register("singer", music_views.SingerViewSet, basename="singer")
music_router.register("song", music_views.SongViewSet, basename="song")
urlpatterns += music_router.urls


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These paths are relative to /api/, which is supplied by the project URLconf.
# <int:pk> captures a numeric primary key and passes it to a detail handler.
# Class-based handlers need as_view(); function-based handlers are passed directly.
# When a router is present, it generates routes and names from a viewset's actions.
# Authentication endpoints, if present, issue/refresh tokens; protect real deployments with HTTPS.
#
# The music router exposes singer/ and song/ under /api/, with names singer-detail and song-detail for hyperlinks.

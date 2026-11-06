from rest_framework.viewsets import ModelViewSet
from .models import Singer, Song
from .music_serializers import SingerSerializer, SongSerializer, SingerStringSerializer, SingerSlugSerializer, SingerLinkSerializer

class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.prefetch_related("song").order_by("id")
    serializer_class = SingerSerializer

    def get_serializer_class(self):
        options = {"string": SingerStringSerializer, "slug": SingerSlugSerializer, "link": SingerLinkSerializer}
        return options.get(self.request.query_params.get("representation"), SingerSerializer)


class SongViewSet(ModelViewSet):
    queryset = Song.objects.select_related("singer").order_by("id")
    serializer_class = SongSerializer


# NOTES ABOUT THE COMPLETE CODE ABOVE
# These viewsets provide the singer/song CRUD routes visible in the relationship lessons.
# prefetch_related fetches reverse collections without a query for each singer.
# select_related joins the single singer relation when loading songs.
# The classroom examples remain available as an additional exercise.

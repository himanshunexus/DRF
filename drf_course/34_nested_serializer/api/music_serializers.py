from rest_framework import serializers
from .models import Singer, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "singer", "duration"]

class SingerSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ["id", "name", "gender", "song"]


# NOTES ABOUT THE COMPLETE CODE ABOVE
# Singer and Song are the domain names visible in the lecture; this implementation is original.
# Song.singer stores one foreign key. related_name="song" exposes a singer's reverse collection.
# A Song POST accepts the singer's database id and validates that it exists.
# In lesson 32, ?representation=string displays song titles using __str__;
# representation=slug displays duration values; representation=link displays detail URLs.
# Without the parameter, lesson 32 returns ids. Duration is a read-only representation,
# not a unique identifier: do not use it for writable relation lookup.
# In lesson 34, song embeds SongSerializer output. This is read-only nesting;
# create songs separately using /api/song/, rather than silently expecting nested saves.
# many=True is essential because one singer can have several songs.
# The companion stores duration in seconds; the sampled code does not establish a unit.

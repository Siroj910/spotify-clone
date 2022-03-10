from rest_framework import serializers
from music.models import Song, Albom, Artist
from rest_framework.exceptions import ValidationError


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'album', 'cover', 'source', 'listened')


    def validate_source(self, value):
        if value.endswith('mp3'):
            raise ValidationError(detail="mp3 bolishi kerak")
        return value
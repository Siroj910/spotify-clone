from django.db import transaction
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from music.serializers import SongSerializer, AlbumSerializer, ArtistSerializer
from music.models import Song, Albom, Artist
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters


class SongViewSet(ModelViewSet):
	queryset = Song.objects.all()
	serializer_class = SongSerializer
	pagination_class = LimitOffsetPagination

	filter_backends = [filters.SearchFilter]
	search_fields = ['title']

	@action(detail=True, methods=['POST'])
	def listen(self, request, *args, **kwargs):
		song = self.get_object()
		with transaction.atomic():
			song.listened +=1
			song.save()
		return Response(status=status.HTTP_204_NO_CONTENT)

	@action(detail=False, methods=['GET'])
	def top(self, request, *args, **kwargs):
		song = self.get_queryset()
		songs = song.order_by('-listened')[:10]
		serializer = SongSerializer(song, many=True)
		return Response(data=serializer.data)


class AlbumViewSet(ModelViewSet):
	queryset = Albom.objects.all()
	serializer_class = AlbumSerializer

class ArtistViewSet(ModelViewSet):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer



	# @action(detail=True): --> detail bu  bironta aniq bir artistga tegishlimi yoki tegishli emasmi yoki bironta
	# obyekta tegishlimi yoki tegishlim emasmi, shunga qarap True yoki False bolad.

	@action(detail=True, methods=["GET"])
	def albums(self, request, *args, **kwargs):
		artist = self.get_object()
		serializer = AlbumSerializer(artist.albom_set.all(), many=True)

		return Response(serializer.data)
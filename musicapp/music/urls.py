from django.urls import path, include
from .views import SongViewSet, AlbumViewSet, ArtistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("songs", SongViewSet)
router.register("album", AlbumViewSet)
router.register("artist", ArtistViewSet)



urlpatterns = [
	path('', include(router.urls)),
]
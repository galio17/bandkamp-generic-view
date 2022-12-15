from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from albums.models import Album

from .models import Song
from .serializers import SongSerializer


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs.get("pk"))
        serializer.save(album=album)

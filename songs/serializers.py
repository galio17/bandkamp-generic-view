from rest_framework.serializers import ModelSerializer

from .models import Song

    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=255)
    # duration = serializers.CharField(max_length=255)
    # album_id = serializers.IntegerField(read_only=True)

class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'album_id']
        read_only_fields = ['album_id']

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

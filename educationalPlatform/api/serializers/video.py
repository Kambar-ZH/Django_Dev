from rest_framework import serializers
from api.models.video import Video
from api.serializers.author import AuthorSerializer


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class VideoDetailSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'

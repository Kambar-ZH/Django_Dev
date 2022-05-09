from rest_framework import serializers
from api.models.video import Video
from api.serializers.author import AuthorSerializer


class VideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()
    preview_url = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = '__all__'

    def get_video_url(self, obj):
        request = self.context.get("request")
        if obj.video_url is None:
            return "None"
        return request.build_absolute_uri(obj.video_url.url)

    def get_preview_url(self, obj):
        request = self.context.get("request")
        if obj.preview_url is None:
            return "None"
        return request.build_absolute_uri(obj.preview_url.url)


class VideoDetailSerializer(VideoSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'

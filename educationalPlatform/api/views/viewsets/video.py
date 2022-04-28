from api.models.video import Video
from api.serializers.video import VideoSerializer
from rest_framework import viewsets


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

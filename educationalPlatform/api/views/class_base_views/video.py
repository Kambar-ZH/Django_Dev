import http
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.video import Video
from api.serializers.video import VideoSerializer

logger = logging.getLogger(__name__)


class VideoAPIView(APIView):
    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND

    def get(self, request, pk):
        video = self.get_object(pk)
        serializer = VideoSerializer(video)
        data = serializer.data
        logger.debug('get video', data)
        return Response(data, http.HTTPStatus.ACCEPTED)

    def put(self, request, pk):
        video = self.get_object(pk)
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug('put video {data}'.format(data=data))
            return Response(serializer.errors, data)
        logger.error('put video {errors}'.format(errors=serializer.errors))
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)


class VideoListAPIView(APIView):
    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        data = serializer.data
        logger.debug('get video list {data}'.format(data=data))
        return Response(data)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug('post video {data}'.format(data=data))
            return Response(serializer.data, http.HTTPStatus.CREATED)
        logger.error('post video {errors}'.format(errors=serializer.errors))
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)

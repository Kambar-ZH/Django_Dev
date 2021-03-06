import http
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.topic import Topic
from api.serializers.topic import TopicSerializer, TopicGridSerializer

logger = logging.getLogger(__name__)


class TopicAPIView(APIView):
    def get_object(self, pk):
        try:
            return Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND

    def get(self, request, pk):
        topic = self.get_object(pk)
        serializer = TopicSerializer(instance=topic, context={'request': request})
        data = serializer.data
        logger.debug('get topic', data)
        return Response(data, http.HTTPStatus.ACCEPTED)

    def put(self, request, pk):
        topic = self.get_object(pk)
        serializer = TopicSerializer(instance=topic, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug('put topic {data}'.format(data=data))
            return Response(data, http.HTTPStatus.ACCEPTED)
        logger.error('put topic {errors}'.format(errors=serializer.errors))
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)


class TopicListAPIView(APIView):
    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicGridSerializer(instance=topics, many=True, context={'request': request})
        data = serializer.data
        logger.debug('get topic list {data}'.format(data=data))
        return Response(data)

    def post(self, request):
        serializer = TopicSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug('post topic {data}'.format(data=data))
            return Response(serializer.data, http.HTTPStatus.CREATED)
        logger.error('post topic {errors}'.format(errors=serializer.errors))
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)

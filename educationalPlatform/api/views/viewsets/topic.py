import logging
from api.models.topic import Topic
from django.shortcuts import get_object_or_404
from api.serializers.topic import TopicSerializer
from rest_framework import viewsets
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class TopicViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Topic.objects.all()
        serializer = TopicSerializer(queryset, many=True)
        data = serializer.data
        logger.debug('get topics', data)
        return Response(data)

    def retrieve(self, request, pk=None):
        queryset = Topic.objects.all()
        topic = get_object_or_404(queryset, pk=pk)
        serializer = TopicSerializer(topic)
        data = serializer.data
        logger.debug('get topic', data)
        return Response(data)


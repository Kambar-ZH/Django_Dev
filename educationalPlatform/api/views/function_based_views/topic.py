import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models.topic import Topic
from api.serializers.topic import TopicGridSerializer

logger = logging.getLogger(__name__)


@api_view(['GET'])
def topic_list_by_course(request, course_id):
    if request.method == 'GET':
        topics = Topic.course_related.get_by_course_without_relation(course_id=course_id)
        serializer = TopicGridSerializer(instance=topics, many=True, context={'request': request})
        data = serializer.data
        logger.debug('get topics by course', data)
        return Response(data)

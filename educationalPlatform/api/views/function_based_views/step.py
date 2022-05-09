import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models.step import Step
from api.serializers.step import StepSerializer

logger = logging.getLogger(__name__)


@api_view(['GET'])
def step_list_by_topic(request, topic_id):
    if request.method == 'GET':
        steps = Step.topic_related.get_by_topic_without_relation(topic_id=topic_id)
        serializer = StepSerializer(instance=steps, many=True, context={'request': request})
        data = serializer.data
        logger.debug('get steps', data)
        return Response(data)

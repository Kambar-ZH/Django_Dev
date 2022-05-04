import http
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.step import Step
from api.serializers.step import StepSerializer, StepDetailSerializer

logger = logging.getLogger(__name__)


class StepAPIView(APIView):
    def get_object(self, pk):
        try:
            return Step.objects.get(pk=pk)
        except Step.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND

    def get(self, request, pk):
        step = self.get_object(pk)
        serializer = StepDetailSerializer(step)
        data = serializer.data
        logger.debug('get step', data)
        return Response(data, http.HTTPStatus.ACCEPTED)

    def put(self, request, pk):
        step = self.get_object(pk)
        serializer = StepSerializer(instance=step, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug('put step {data}'.format(data=data))
            return Response(data, http.HTTPStatus.ACCEPTED)
        logger.error('put step {errors}'.format(errors=serializer.errors))
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)


class StepListAPIView(APIView):
    def get(self, request):
        steps = Step.objects.all()
        serializer = StepSerializer(steps, many=True)
        data = serializer.data
        logger.debug('get step list {data}'.format(data=data))
        return Response(data)

    def post(self, request):
        serializer = StepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug('post step {data}'.format(data=data))
            return Response(serializer.data, http.HTTPStatus.CREATED)
        logger.error('post step {errors}'.format(errors=serializer.errors))
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)

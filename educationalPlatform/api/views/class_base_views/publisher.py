import http
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.publisher import Publisher
from api.serializers.publisher import PublisherSerializer

logger = logging.getLogger(__name__)


class PublisherAPIView(APIView):
    def get_object(self, pk):
        try:
            return Publisher.objects.get(pk=pk)
        except Publisher.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND

    def get(self, request, pk):
        publisher = self.get_object(pk)
        serializer = PublisherSerializer(publisher)
        data = serializer.data
        logger.debug('get publisher', data)
        return Response(data, http.HTTPStatus.ACCEPTED)

    def put(self, request, pk):
        publisher = self.get_object(pk)
        serializer = PublisherSerializer(instance=publisher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug('put publisher {data}'.format(data=data))
            return Response(data, http.HTTPStatus.ACCEPTED)
        logger.error('put publisher {errors}'.format(errors=serializer.errors))
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)


class PublisherListAPIView(APIView):
    def get(self, request):
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        data = serializer.data
        logger.debug('get publisher list {data}'.format(data=data))
        return Response(data)

    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug('post publisher {data}'.format(data=data))
            return Response(serializer.data, http.HTTPStatus.CREATED)
        logger.error('post publisher {errors}'.format(errors=serializer.errors))
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)

import http
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.author import Author
from api.serializers.author import AuthorSerializer

logger = logging.getLogger(__name__)


class AuthorAPIView(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND

    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        data = serializer.data
        logger.debug('get author', data)
        return Response(data, http.HTTPStatus.ACCEPTED)

    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug('put author {data}'.format(data=data))
            return Response(serializer.errors, data)
        logger.error('put author {errors}'.format(errors=serializer.errors))
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)


class AuthorListAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        data = serializer.data
        logger.debug('get author list {data}'.format(data=data))
        return Response(data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug('post author {data}'.format(data=data))
            return Response(serializer.data, http.HTTPStatus.CREATED)
        logger.error('post author {errors}'.format(errors=serializer.errors))
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)

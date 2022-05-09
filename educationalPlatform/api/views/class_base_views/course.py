import http
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.course import Course
from api.serializers.course import CourseSerializer, CourseGridSerializer

logger = logging.getLogger(__name__)


class CourseAPIView(APIView):
    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(instance=course, context={'request': request})
        data = serializer.data
        logger.debug('get course', data)
        return Response(data, http.HTTPStatus.ACCEPTED)

    def put(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(instance=course, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug('put course {data}'.format(data=data))
            return Response(data, http.HTTPStatus.ACCEPTED)
        logger.error('put course {errors}'.format(errors=serializer.errors))
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)


class CourseListAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseGridSerializer(instance=courses, many=True, context={'request': request})
        data = serializer.data
        logger.debug('get course list {data}'.format(data=data))
        return Response(data=data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug('post course {data}'.format(data=data))
            return Response(serializer.data, http.HTTPStatus.CREATED)
        logger.error('post course {errors}'.format(errors=serializer.errors))
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)

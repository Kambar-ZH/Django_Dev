import logging
from api.models.course import Course
from django.shortcuts import get_object_or_404
from api.serializers.course import CourseSerializer, CourseGridSerializer
from rest_framework import viewsets
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class CourseViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Course.objects.all()
        serializer = CourseGridSerializer(queryset, many=True)
        data = serializer.data
        logger.debug('get courses', data)
        return Response(data)

    def retrieve(self, request, pk=None):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course)
        data = serializer.data
        logger.debug('get course', data)
        return Response(data)


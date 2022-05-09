import http
import logging

from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count
from api.models.course import Course
from api.serializers.course import CourseSerializer, CourseGridSerializer
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

authentication_classes = (TokenAuthentication,)
permission_classes = (IsAuthenticated,)


@api_view(['GET'])
def course_list_by_publisher(request, publisher_id):
    if request.method == 'GET':
        courses = Course.publisher_related.get_by_publisher_without_relation(publisher_id)
        serializer = CourseSerializer(instance=courses, many=True, context={'request': request})
        data = serializer.data
        logger.debug('get courses by publisher', data)
        return Response(data)


@api_view(['GET'])
def course_list_by_category(request, category):
    if request.method == 'GET':
        courses = Course.publisher_related.get_by_category(category)
        serializer = CourseSerializer(instance=courses, many=True, context={'request': request})
        data = serializer.data
        logger.debug('get courses by category', data)
        return Response(data)


@api_view(['GET'])
def course_list_most_rated(request):
    if request.method == 'GET':
        courses = Course.objects.all().annotate(num_user=Count('likes')).order_by('-num_user')[:10]
        serializer = CourseGridSerializer(instance=courses, many=True, context={'request': request})
        data = serializer.data
        logger.debug('get top rated courses', data)
        return Response(data)


@api_view(['POST'])
def course_subscribe(request, pk):
    if request.method == 'POST':
        course = Course.objects.get(pk=pk)
        user = User.objects.get(username=request.user)
        course.users.add(user)
        return Response(status=http.HTTPStatus.CREATED)


@api_view(['POST'])
def course_like(request, pk):
    if request.method == 'POST':
        course = Course.objects.get(pk=pk)
        user = User.objects.get(username=request.user)
        course.likes.add(user)
        return Response(status=http.HTTPStatus.CREATED)


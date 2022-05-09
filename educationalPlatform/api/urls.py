from django.urls import path, include
from rest_framework import routers

from api.views.viewsets.topic import TopicViewSet
from api.views.viewsets.course import CourseViewSet
from api.views.class_base_views.signup import SignupView
from api.views.class_base_views.step import StepAPIView, StepListAPIView
from api.views.class_base_views.topic import TopicAPIView, TopicListAPIView
from api.views.class_base_views.video import VideoAPIView, VideoListAPIView
from api.views.class_base_views.author import AuthorAPIView, AuthorListAPIView
from api.views.class_base_views.course import CourseAPIView, CourseListAPIView
from api.views.class_base_views.publisher import PublisherAPIView, PublisherListAPIView
from api.views.function_based_views.course import *
from api.views.function_based_views.topic import *
from api.views.function_based_views.step import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register('topic-viewset', TopicViewSet, basename='Topic')
router.register('course-viewset', CourseViewSet, basename='Course')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('signup/', SignupView.as_view()),
    path('authors/<int:pk>/', AuthorAPIView.as_view()),
    path('authors/', AuthorListAPIView.as_view()),
    path('courses/<int:pk>/', CourseAPIView.as_view()),
    path('courses/', CourseListAPIView.as_view()),
    path('publishers/<int:publisher_id>/courses/', course_list_by_publisher),
    path('courses/by_category/<int:category>/', course_list_by_category),
    path('courses/most_rated/', course_list_most_rated),
    path('courses/subscribe/', course_subscribe),
    path('courses/<int:pk>/like/', course_like),
    path('topics/<int:pk>/', TopicAPIView.as_view()),
    path('topics/', TopicListAPIView.as_view()),
    path('courses/<int:course_id>/topics/', topic_list_by_course),
    path('steps/<int:pk>/', StepAPIView.as_view()),
    path('steps/', StepListAPIView.as_view()),
    path('topics/<int:topic_id>/steps/', step_list_by_topic),
    path('publishers/<int:pk>/', PublisherAPIView.as_view()),
    path('publishers/', PublisherListAPIView.as_view()),
    path('videos/<int:pk>/', VideoAPIView.as_view()),
    path('videos/', VideoListAPIView.as_view()),
]

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
from api.views.function_based_views.course import course_list_by_category, course_list_by_publisher, \
    course_list_most_rated
from api.views.function_based_views.topic import topic_list_by_course
from api.views.function_based_views.step import step_list_by_topic

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register('topic-viewset', TopicViewSet, basename='Topic')
router.register('course-viewset', CourseViewSet, basename='Course')

urlpatterns = [
    path('/', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('signup/', SignupView.as_view()),
    path('authors/<int:pk>/', AuthorAPIView.as_view()),
    path('authors/', AuthorListAPIView.as_view()),
    path('courses/<int:pk>/', CourseAPIView.as_view()),
    path('courses/', CourseListAPIView.as_view()),
    path('courses/by_publisher/<int:publisher_id>', course_list_by_publisher),
    path('courses/by_category/<int:category>', course_list_by_category),
    path('courses/most_rated', course_list_most_rated),
    path('topics/<int:pk>/', TopicAPIView.as_view()),
    path('topics/', TopicListAPIView.as_view()),
    path('topics/by_step/<int:step_id>', topic_list_by_course),
    path('steps/<int:pk>/', StepAPIView.as_view()),
    path('steps/', StepListAPIView.as_view()),
    path('steps/by_topic/<int:topic_id>', step_list_by_topic),
    path('publishers/<int:pk>/', PublisherAPIView.as_view()),
    path('publishers/', PublisherListAPIView.as_view()),
    path('videos/<int:pk>/', VideoAPIView.as_view()),
    path('videos/', VideoListAPIView.as_view()),
]

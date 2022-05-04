from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main.views.viewsets import *
from main.views.views_fbv import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register('todo_lists', TodoListViewSet, basename='TodoLists')
router.register('todos', TodoViewSet, basename='Todos')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('todo_lists/<int:todo_list_id>/todos/', get_todos_by_todo_list),
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

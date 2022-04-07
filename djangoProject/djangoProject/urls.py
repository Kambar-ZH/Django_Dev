from django.contrib import admin
from django.urls import path

from main.views.views_cbv import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/<int:list_id>/', ListView.as_view()),
    path('todos/<int:list_id>/completed/', CompletedListView.as_view()),
    path('todos/<int:list_id>/todo/<int:todo_id>/', TodoView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

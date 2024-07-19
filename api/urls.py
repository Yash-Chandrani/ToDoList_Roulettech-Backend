from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, register, login, change_password, delete_account

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', register),
    path('api/login/', login),
    path('api/change-password/', change_password),
    path('api/delete-account/', delete_account),
]

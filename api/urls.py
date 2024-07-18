from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, register, login

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', register),
    path('api/login/', login),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, register, login, change_password, delete_account
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

schema_view = get_schema_view(
    openapi.Info(
        title="ToDo List API",
        default_version='v1',
        description="API documentation for the ToDo List application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', register),
    path('api/login/', login),
    path('api/change-password/', change_password),
    path('api/delete-account/', delete_account),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

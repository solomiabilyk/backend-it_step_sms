from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from students.views import StudentViewSet
from lessons.views import LessonViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

router = DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"lessons", LessonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('users.urls')),

    path('api/', include(router.urls)),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
]
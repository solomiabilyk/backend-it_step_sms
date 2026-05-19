from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from students.views import StudentViewSet
from lessons.views import LessonViewSet
from branches.views import BranchViewSet
from subscriptions.views import (
    SubscriptionPlanViewSet,
    StudentSubscriptionViewSet
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from attendance.views import AttendanceViewSet
from subjects.views import SubjectViewSet

router = DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"lessons", LessonViewSet)
router.register(r"attendance", AttendanceViewSet)
router.register(r"subjects", SubjectViewSet)
router.register(r"branches", BranchViewSet)
router.register(r"subscription-plans", SubscriptionPlanViewSet)
router.register(r"student-subscriptions", StudentSubscriptionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('users.urls')),

    path('api/', include(router.urls)),

    # JWT
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    # Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
]
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CourseViewSet


router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls)),
]

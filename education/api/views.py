from django.shortcuts import render


from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny

from api.serializers import CourseSerializer
from courses.models import Course


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.select_related(
        "level"
        ).order_by("level__period")
    permission_classes = (AllowAny,)

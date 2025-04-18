from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny

from api.serializers import CourseSerializer


class CourseViewSet(viewsets.Modelviewset):
    serializer_class = CourseSerializer
    # queryset = Course.objects.all()
    permission_classes = (AllowAny,)

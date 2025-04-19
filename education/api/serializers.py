from rest_framework import serializers

from courses.models import Course, Level


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    level = LevelSerializer(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

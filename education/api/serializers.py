from rest_framework import serializers


class CourseSerializer(serializers.ModelField):

    class Meta:
        model = Course
        fields = "__all__"

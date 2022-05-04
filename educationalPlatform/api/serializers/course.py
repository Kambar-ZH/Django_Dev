from rest_framework import serializers
from api.models.course import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseGridSerializer(serializers.ModelSerializer):
    publisher_name = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'created', 'publisher_name', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_publisher_name(self, obj):
        return obj.publisher.full_name

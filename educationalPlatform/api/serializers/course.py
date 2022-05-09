from rest_framework import serializers
from api.models.course import Course


class CourseSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_category(self, obj):
        return obj.get_category_display()


class CourseGridSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    publisher_name = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    subscribers_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'created', 'publisher_name', 'likes_count', 'subscribers_count']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_publisher_name(self, obj):
        return obj.publisher.full_name

    def get_subscribers_count(self, obj):
        return obj.users.count()

    def get_category(self, obj):
        return obj.get_category_display()
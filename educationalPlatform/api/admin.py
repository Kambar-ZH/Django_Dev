from django.contrib import admin
from api.models.author import Author
from api.models.course import Course
from api.models.topic import Topic
from api.models.step import Step
from api.models.publisher import Publisher
from api.models.video import Video


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'category', 'created']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'address', 'city', 'country', 'website']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'views']

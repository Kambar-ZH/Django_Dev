from django.db import models
from api.models.course import Course
from api.managers.topic import TopicManager


class Topic(models.Model):
    title = models.CharField(max_length=200, blank=False)
    course = models.ForeignKey(Course, blank=False, on_delete=models.CASCADE)

    objects = models.Manager()
    course_related = TopicManager()

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['title']

    def __str__(self):
        return f'{self.id}: {self.title}'

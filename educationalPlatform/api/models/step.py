from django.db import models
from api.models.video import Video
from api.models.topic import Topic
from api.managers.step import StepManager


class Step(models.Model):
    description = models.TextField()
    topic = models.ForeignKey(Topic, blank=False, on_delete=models.CASCADE)
    videos = models.OneToOneField(Video, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()
    topic_related = StepManager()

    class Meta:
        verbose_name = 'Шаг'
        verbose_name_plural = 'Шаги'

    def __str__(self):
        return f'{self.id}: {self.description}'

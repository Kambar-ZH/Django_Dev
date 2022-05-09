import datetime

from django.db import models
from api.models.author import Author
from api.utils.upload import *
from api.utils.validators import *


class Video(models.Model):
    preview_url = models.ImageField(upload_to=image_directory_path,
                                    validators=[validate_image_size, validate_image_extension],
                                    blank=False)
    video_url = models.FileField(upload_to=video_file_directory_path,
                                 validators=[validate_file_size, validate_file_extension],
                                 blank=False)
    uploaded = models.DateField(editable=True, default=datetime.date.today)
    title = models.CharField(max_length=200, blank=False)
    views = models.IntegerField(default=0)
    authors = models.ManyToManyField(Author)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['title']

    def __str__(self):
        return f'{self.id}: {self.title}'

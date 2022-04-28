import datetime

import django.utils.timezone
from django.db import models
from api.models.author import Author
from api.models.publisher import Publisher
from django.contrib.auth.models import User
from api.managers.course import CourseManager
from api.utils.constants import COURSE_CATEGORIES, ALGORITHMS


class Course(models.Model):
    title = models.CharField(max_length=500, blank=False)
    description = models.TextField(blank=False)
    category = models.PositiveSmallIntegerField(choices=COURSE_CATEGORIES, default=ALGORITHMS)
    created = models.DateField(editable=True, default=django.utils.timezone.now())

    authors = models.ManyToManyField(Author, blank=True)
    users = models.ManyToManyField(User, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='liker_id')
    publisher = models.OneToOneField(Publisher, blank=True, on_delete=models.PROTECT)

    objects = models.Manager()
    publisher_related = CourseManager()

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-created']

    def __str__(self):
        return f'{self.id}: {self.title}'

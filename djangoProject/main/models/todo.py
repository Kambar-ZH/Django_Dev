import datetime

from django.db import models

from main.managers.todo import TodoManager
from main.models.todo_list import TodoList
from main.utils.upload import *
from main.utils.validators import *


class Todo(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateField(default=datetime.date.today)
    due = models.DateField(default=datetime.date.today)
    owner = models.CharField(max_length=30, blank=True, null=True)
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_directory_path,
                              validators=[validate_image_size, validate_image_extension],
                              blank=True, null=True)
    file = models.ImageField(upload_to=file_directory_path,
                             validators=[validate_file_size, validate_file_extension],
                             blank=True, null=True)

    objects = models.Manager()
    todo_related = TodoManager()

from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=255)
    favorite = models.BooleanField(default=False)

from django.db import models


class List(models.Model):
    name = models.CharField(max_length=255)


class Todo(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField()
    due_on = models.DateField()
    owner = models.CharField(max_length=30)
    is_done = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

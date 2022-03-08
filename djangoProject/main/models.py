from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField()
    due_on = models.DateField()
    owner = models.CharField(max_length=30)
    is_done = models.BooleanField(default=False)
    list_id = models.IntegerField(default=1)

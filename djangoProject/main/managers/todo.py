from django.db import models


class TodoManager(models.Manager):
    def get_by_todo_list_without_relation(self, todo_list_id):
        return self.filter(todo_list_id=todo_list_id)

    def get_related(self):
        return self.select_related('topic')

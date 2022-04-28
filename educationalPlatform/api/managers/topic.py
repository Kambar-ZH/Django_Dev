from django.db import models


class TopicManager(models.Manager):
    def get_by_course_without_relation(self, course_id):
        return self.filter(course_id=course_id)

    def get_related(self):
        return self.select_related('course')

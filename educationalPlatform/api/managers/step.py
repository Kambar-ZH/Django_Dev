from django.db import models


class StepManager(models.Manager):
    def get_by_topic_without_relation(self, topic_id):
        return self.filter(topic_id=topic_id)

    def get_related(self):
        return self.select_related('topic')

from django.db import models


class CourseManager(models.Manager):
    def get_by_category(self, category):
        return self.filter(category=category)

    def get_by_publisher_without_relation(self, publisher_id):
        return self.filter(publisher_id=publisher_id)

    def get_related(self):
        return self.select_related('publisher')

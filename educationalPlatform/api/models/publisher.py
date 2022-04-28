from django.db import models


class Publisher(models.Model):
    full_name = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    website = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'
        ordering = ['full_name']

    def __str__(self):
        return f'{self.id}: {self.full_name}'

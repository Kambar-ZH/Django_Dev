from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=200, blank=False)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['first_name']

    def __str__(self):
        return f'{self.id}: {self.first_name}, {self.last_name}'

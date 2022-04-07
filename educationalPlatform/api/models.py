from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)


class Course(models.Model):
    name = models.CharField(max_length=500, blank=False)
    description = models.TextField(blank=False)
    created = models.DateField(auto_now_add=True)
    authors = models.ManyToManyField(Author, on_delete=models.CASCADE, blank=False)
    likes = models.IntegerField(default=0)



class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    password = models.TextField(blank=False)


class Topic(models.Model):
    name = models.CharField(max_length=200, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False)


class Video(models.Model):
    path = models.CharField(max_length=1000, blank=False)
    name = models.CharField(max_length=200, blank=False)
    views = models.IntegerField(default=0)


class Step(models.Model):
    description = models.TextField()
    videos = models.OneToOneField(Video, on_delete=models.CASCADE, null=True, blank=True)
    files = models.CharField()


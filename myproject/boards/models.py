from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Topic(models.Model): 
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')

class Tag(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'tags'


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')


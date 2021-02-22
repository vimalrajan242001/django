from django.db import models


class Post(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField()
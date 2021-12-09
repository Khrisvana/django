from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()
    posted_at = models.DateTimeField(timezone.now)



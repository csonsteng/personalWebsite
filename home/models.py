from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    img = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    body = models.TextField()

    def __str__(self):
        return self.title
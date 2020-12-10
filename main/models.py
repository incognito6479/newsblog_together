from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    post_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

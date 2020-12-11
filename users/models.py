from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='static/default.png', upload_to='static', validators=[file_size])


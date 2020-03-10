# pylint: disable=no-member,arguments-differ
from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_email
# from items.models import Item


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(null=True, validators=[validate_email])
    profile_image = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.username

class Recommendation(models.Model):
    text = models.CharField(max_length=200, blank=True)
    from_user = models.ForeignKey(
        User,
        related_name='recommendations',
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    def __str__(self):
        return f'Recommendation from {self.from_user}'

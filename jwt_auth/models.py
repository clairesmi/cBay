# pylint: disable=no-member

from django.db import models
from django.contrib.auth.models import AbstractUser
# from items.models import Item
from .validators import validate_email

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

class Listing(models.Model):
    listed_item = models.OneToOneField(
        'items.Item',
        related_name='listings',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True)
    owner = models.ForeignKey(
        User,
        related_name='listings',
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    def __str__(self):
        return  f'{self.owner.username}s Listings'

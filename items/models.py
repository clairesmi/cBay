# pylint: disable=no-member,arguments-differ
from django.db import models
from jwt_auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    category_image = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    size = models.CharField(max_length=50, default='')
    image = models.CharField(max_length=500)
    buyer = models.CharField(max_length=500, default='')
    categories = models.ManyToManyField(
        Category,
        related_name='items',
        blank=True
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='items',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    basket = models.ForeignKey(
        User,
        related_name='basket_items',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Item {self.name}'


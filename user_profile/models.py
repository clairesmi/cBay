from django.db import models
from jwt_auth.models import User
from items.models import Item

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,
    related_name='user_profile',
    on_delete=models.CASCADE,
    primary_key=True),
    items_posted = models.ForeignKey(Item,
    related_name='user_profile',
    on_delete=models.DO_NOTHING,
    blank=True)

def __str__(self):
    return self.user

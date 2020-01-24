from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_email

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(null=True, validators=[validate_email])

    def __str__(self):
        return self.username
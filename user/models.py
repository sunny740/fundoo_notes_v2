from email.policy import default
from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import JWTService

class User(AbstractUser):
    phone_number = models.BigIntegerField()
    location = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)

    # @property
    def tokens(self):
        return JWTService().encode_token({"user_id": self.id, "username": self.username})

class UserLog(models.Model):
    url = models.CharField(max_length=100)
    method = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)
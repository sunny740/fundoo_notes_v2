from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import JWTService

class User(AbstractUser):
    phone_number = models.BigIntegerField()
    location = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)

    def tokens(self):
        return JWTService.encode_token({"user_id": self.userid, "username": self.username})

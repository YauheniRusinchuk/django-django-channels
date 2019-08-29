from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


User = get_user_model()


class Profile(models.Model):
    user             = models.OneToOneField(User, on_delete=models.CASCADE)
    description      = models.TextField(blank=True)


    def __str__(self):
        return f"Profile {self.user.username}"

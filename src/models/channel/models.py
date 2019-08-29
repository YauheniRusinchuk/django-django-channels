from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Channel(models.Model):
    name        = models.CharField(max_length=255, blank=False)
    password    = models.CharField(max_length=300, blank=True)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    peoples     = models.ManyToManyField(User, related_name='members', symmetrical=False, blank=True)
    create      = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name}"

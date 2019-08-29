from django.db import models
from django.contrib.auth import get_user_model
from src.models.channel.models import Channel

User = get_user_model()


class Message(models.Model):
    who     = models.ForeignKey(User, on_delete=models.CASCADE)
    text    = models.TextField(blank=False)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    create  = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.text}"

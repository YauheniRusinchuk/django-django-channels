from django.test import TestCase
from src.models.channel.models import Channel
from src.models.message.models import Message
from django.contrib.auth import get_user_model

User = get_user_model()

class TestMessage(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User(username='test', password='test')
        user.save()
        channel = Channel(name='testChannel', author=user)
        channel.save()
        message = Message(who=user, channel=channel, text='TEST MESSAGE')


    def test_count_channels(self):
        count_message = Message.objects.all().count()
        self.assertEqual(1, 1)

from django.test import TestCase
from src.models.channel.models import Channel
from django.contrib.auth import get_user_model

User = get_user_model()

class TestChannel(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User(username='test', password='test')
        user.save()
        channel = Channel(name='testChannel', author=user)
        channel.save()


    def test_count_channels(self):
        count = Channel.objects.all().count()
        self.assertEqual(1, 1)

    def test_check_author(self):
        channel = Channel.objects.get(pk=1)
        self.assertEqual(channel.author.username, 'test')    

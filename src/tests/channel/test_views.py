from django.test import TestCase, Client
from django.urls import reverse
from src.models.channel.models import Channel
from django.contrib.auth import get_user_model

User = get_user_model()



class TestChannelViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home:home_page')
        self.detail_url = reverse('detail:detail_page', args=[1])

    def test_channel_view_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 302)


    def test_channel_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 302)

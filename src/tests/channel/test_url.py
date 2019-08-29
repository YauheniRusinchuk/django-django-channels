from django.test import TestCase
from django.urls import reverse, resolve
from src.apps.home.views import Index
from src.apps.newchannel.views import NewChannel
from src.apps.detailchannel.views import Detail


class TestUrls(TestCase):

    def test_list_channels_url(self):
        url = reverse('home:home_page')
        self.assertEqual(resolve(url).func.view_class, Index)

    def test_add_channel_url(self):
        url = reverse('newchannel:newchannel_page')
        self.assertEqual(resolve(url).func.view_class, NewChannel)

    def test_detail_channel(self):
        url = reverse('detail:detail_page', args=[1])
        self.assertEqual(resolve(url).func.view_class, Detail)

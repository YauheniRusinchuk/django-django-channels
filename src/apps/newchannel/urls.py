from django.urls import path
from .views import NewChannel

app_name = 'newchannel'

urlpatterns = [
    path('', NewChannel.as_view(), name='newchannel_page'),
]

from django.urls import path
from .views import Profile


app_name = 'profile'


urlpatterns = [
    path('<str:name>/', Profile.as_view(), name='profile_page'),
]

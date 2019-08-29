from django.urls import path
from .views import Index
from src.apps.login.views import exit

app_name = 'home'

urlpatterns = [
    path('logout/', exit, name='exit_page'),
    path('', Index.as_view(), name='home_page'),
]

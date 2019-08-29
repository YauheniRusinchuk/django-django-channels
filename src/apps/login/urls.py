from django.urls import path
from .views import Login

app_name = 'login'

urlpatterns = [
    path('', Login.as_view(), name='login_page'),
]

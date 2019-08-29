from django.urls import path
from .views import Detail, Check

app_name = 'detail'

urlpatterns = [
    path('<int:pk>/', Detail.as_view(), name='detail_page'),
    path('<int:pk>/checkpassword/', Check.as_view(), name='check_page'),
]

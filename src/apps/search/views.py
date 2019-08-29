from django.views import View
from django.shortcuts import render
from django.contrib.auth import get_user_model
from src.models.channel.models import Channel


User = get_user_model()

class Search(View):

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            users = Channel.objects.filter(name__icontains=query)
            print(users)
        return render(request, 'search/search.html', {'users': users})

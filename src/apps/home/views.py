from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from src.models.channel.models import Channel


class Index(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            channels = Channel.objects.all()
            return render(request, 'home/index.html', {'channels': channels})
        return HttpResponseRedirect('/login/')

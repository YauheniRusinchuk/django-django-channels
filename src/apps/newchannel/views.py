from django.views import View
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from src.models.channel.models import Channel

class NewChannel(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'newchannel/newchannel.html', {})


    def post(self, request, *args, **kwargs):
        name        = request.POST.get('name')
        password    = request.POST.get('password')
        channel     = Channel()
        user        = request.user
        if name and password:
            hashed_pswd = make_password(password)
            channel.name = name
            channel.author = user
            channel.password = hashed_pswd
            channel.save()
            return HttpResponse()
        elif name:
                channel.name = name
                channel.author = user
                channel.save()
                return HttpResponse()
        else:
            return HttpResponseBadRequest()

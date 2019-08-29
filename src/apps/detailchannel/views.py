from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from src.models.channel.models import Channel
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, reverse, get_object_or_404, redirect


class Detail(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            channel = get_object_or_404(Channel, pk=kwargs.get('pk'))
            if not channel.password:
                return render(request, 'detailchannel/detail.html', {'channel': channel})
            if self.request.user == channel.author or self.request.user in channel.peoples.all():
                return render(request, 'detailchannel/detail.html', {'channel': channel})
            else:
                return redirect(reverse('detail:check_page', kwargs={'pk': channel.pk}))
        else:
            return HttpResponseRedirect('/login/')




class Check(View):

    def get(self, request, *args, **kwargs):
        channel = get_object_or_404(Channel, pk=kwargs.get('pk'))
        if self.request.user == channel.author or self.request.user in channel.peoples.all():
            return render(request, 'detailchannel/detail.html', {'channel': channel})
        return render(request, 'detailchannel/checkpassword.html', {})


    def post(self, request, *args, **kwargs):
        channel = get_object_or_404(Channel, pk=kwargs.get('pk'))
        password = request.POST.get('password')
        if check_password(password, channel.password):
            channel.peoples.add(request.user)
            return HttpResponse()
        return HttpResponseBadRequest()

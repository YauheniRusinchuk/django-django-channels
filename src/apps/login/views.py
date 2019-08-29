from django.views import View
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout



class Login(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, 'login/login.html', {})


    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('good')
        return HttpResponseNotFound('bad')


def exit(request):
    logout(request)
    return HttpResponseRedirect('/')

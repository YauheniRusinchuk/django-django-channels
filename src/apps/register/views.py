from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.contrib.auth import get_user_model, login
from src.models.profile.models import Profile

User = get_user_model()


class Register(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, 'register/register.html', {})


    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if qs.exists():
                return HttpResponseNotFound('bad')
            user = User(username=username)
            user.set_password(password)
            user.save()
            profile = Profile(user=user)
            profile.save()
            login(request, user)
            return HttpResponse('good')
        else:
            return HttpResponseNotFound('bad')

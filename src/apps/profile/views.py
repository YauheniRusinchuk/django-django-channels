from django.views import View
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(View):

    def get(self, request, *args, **kwargs):
        name = kwargs.get('name')
        user = User.objects.get(username=name)
        return render(request, 'profile/profile.html', {"profile": user})



class EditProfile(View):
    pass

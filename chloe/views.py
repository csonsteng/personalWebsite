from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login(request):
    username = request.POST['user']
    password = request.POST['pass']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return accounts(request)
    else:
        context={
            'fail': 'incorrect username or password.',
            }
        return render(request, 'login.html', context)
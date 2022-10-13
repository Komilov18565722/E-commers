import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.accountsForm import AccountsForm
from accounts.models import CustomUser
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if request.POST.get('email'):
            user = AccountsForm(request.POST)
            if user.is_valid():
                user = user.save(commit = False)
                user.save()
                login(request, user)
                return redirect('home')
            else:
                print('0000000000000000000000000000000000000000000000')
                return redirect('login')   
        else:
            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                messages.success(request, ("Success login!"))
                return redirect('home')
            else:
                messages.warning(request, ("Your Password or Username faild"))
                return redirect('login')
    else:
        return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')
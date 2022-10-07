import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.models import CustomUser
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if request.POST.get('email'):
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            number = request.POST['phone']
            age = request.POST['age']
            try:
                

                user = CustomUser.objects.create_user( username = username,
                                            first_name=fname,
                                            last_name=lname,
                                            email=email,
                                            phone_number=number, 
                                            age = age, 
                                            password=password
                )
                user.save()
                login(request, user)
                return redirect('home')
            
            except:
                if username and password and fname and lname and email:
                    messages.success(request, ("This Username is already registered"))
                else:
                    messages.success(request, ("The information is incomplete"))
                return redirect('login')

            
        else:
            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                messages.success(request, ("Success login!"))
                return redirect('home')
            else:
                messages.success(request, ("Your Password or Username faild"))
                return redirect('login')
    else:
        return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')
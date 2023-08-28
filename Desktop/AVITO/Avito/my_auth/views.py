from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

 
 
def reg_view(request):
 return render(request, 'app_auth/register.html') 
 
def profile_view(request):
 return render(request,'app_auth/profile.html')

@login_required(login_url=reverse_lazy('log')) 
def login_view(request):
    redirect_url = reverse('prof')
    if request.neathod == "GET":
        if request.user_authenticated:        # Username !== AnonyomousUser=           
           return redirect(redirect_url)
        else:
          return render(request,'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login', {"error": 'Пользователь не найден.'})  

def logout_view(request):
    logout(request)
    return redirect(reverse('log'))
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
 return render(request, 'index.html')
 
def topSellers(request):
 return render(request,'top-sellers.html')
   
def register(request):
 return render(request, 'register.html') 
 
def login(request):
 return render(request,'login.html')
 
def profile(request):
 return render(request,'profile.html')
 

def advertisement(request):
 return render(request, 'advertisement.html')


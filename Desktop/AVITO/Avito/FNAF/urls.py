from django.urls import path
from .views import *
from  django.shortcuts import render
urlpatterns = [
   path('',index, name='main.page'),
   path('liders', topSellers, name='top-sellers'),
   path('maximus',register, name='register'),
   path('randof',profile, name='profile'),
   path('nigers', login, name='login'),
   path('snake', adversiment, name='adversiment'),
   path('butovskiy',advertisement-post , name='advertisement-post')
 ]  
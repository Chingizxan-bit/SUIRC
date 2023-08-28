from django.urls import path
from .views import *
from  django.shortcuts import render
urlpatterns = [
   path('',index, name='main.page'),
   path('liders', topSellers , name='top-sellers'),
   path('advertPost', AdvertsForm , name='advertisement-post'),
 ] 
# ссылка на которую будет вести ,представление ,имя 
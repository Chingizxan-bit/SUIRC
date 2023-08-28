from django.urls import path
from .views import *

urlpatterns = [  
   path('register', reg_view, name='reg'),
   path('profile', profile_view, name='prof'),
   path('login', login_view, name='log'),
   path('logout', logout_view, name='logout'),
  ]
   
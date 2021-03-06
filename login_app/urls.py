""" Handles all of the specific url routes of the login_app,
queries from db or templates that need to be rendered. """ 



""" links specific URL(urlpath) to the defined views(urlHandler)."""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.register,name='signup'),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('homepage/', views.home,  name='homepage'),
    
]

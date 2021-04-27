from django.urls import path

from . import views

urlpatterns = [
    path('', views.login),
    path('register', views.register),
    path('user/create', views.create_user),
    path('user/user_login', views.user_login),
    path('logout', views.logout)
    ]

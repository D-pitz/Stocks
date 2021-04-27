from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('user_account', views.display_user_account),
    path('stock_page', views.display_stock_page)
    ]
from django.contrib import admin
from django.urls import path

from . import views, views_users

urlpatterns = [
    path('', views.index, name='person'),
    path("register/", views.register, name="register_person"),
    path("pay-reg-fees/", views.pay_fees, name="pay-reg-fees"),

    path("users/", views_users.index, name="users"),
    path("users/add", views_users.add, name="user_add"),
    path("users/<int:pk>/delete", views_users.delete, name="user_delete"),
    path("users/<int:pk>", views_users.detail, name="user_detail"),
    
]
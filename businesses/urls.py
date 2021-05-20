from django.contrib import admin
from django.urls import path

from businesses import views, views_users

urlpatterns = [
    path('', views.index, name='business'),
    path("register/", views.register, name="register_business"),
    path("pay-reg-fees/", views.pay_fees, name="pay-reg-fees"),

    path("users/", views_users.index, name="users"),
    path("users/add", views_users.add, name="add_user"),
    path("users/<int:pk>/delete", views_users.delete, name="delete_user"),
    path("users/<int:pk>", views_users.view, name="view_user"),
    
]
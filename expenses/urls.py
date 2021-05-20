from django.urls import path 
from expenses import views

urlpatterns = [
    path('', views.index, name="expenses"),
    path("add/", views.expense_add, name="expense_add"),
    path("<int:pk>/change/", views.expense_change, name="expense_change"),
    path("<int:pk>/", views.expense_detail, name="expense_detail"),
    path("<int:pk>/delete/", views.expense_delete, name="expense_delete")
]
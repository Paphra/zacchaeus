from django.urls import path, include
from . import views_closing as views

urlpatterns = [
    path("", views.index, name="closing_stocks"),
    path("add/", views.add, name="closing_stock_add"),
    path("<int:pk>/", views.detail, name="closing_stock_detail"),
    path("<int:pk>/change/", views.change, name="closing_stock_change"),
    path("<int:pk>/delete/", views.delete, name="closing_stock_delete"),
]

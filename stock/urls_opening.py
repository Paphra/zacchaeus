from django.urls import path, include
from . import views_opening as views 

urlpatterns = [
    path("", views.index, name="opening_stocks"),
    path("add/", views.add, name="opening_stock_add"),
    path("<int:pk>/", views.detail, name="opening_stock_detail"),
    path("<int:pk>/change/", views.change, name="opening_stock_change"),
    path("<int:pk>/delete/", views.delete, name="opening_stock_delete"),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="sales"),
    path("add/", views.add, name="sale_add"),
    path("<int:pk>/", views.detail, name="sale_detail"),
    path("<int:pk>/change/", views.change, name="sale_change"),
    path("<int:pk>/delete/", views.delete, name="sale_delete"),

    path("returns/", include('sales.urls_returns')),
]
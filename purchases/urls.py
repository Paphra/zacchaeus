from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="purchases"),
    path("add/", views.add, name="purchase_add"),
    path("<int:pk>/", views.detail, name="purchase_detail"),
    path("<int:pk>/change/", views.change, name="purchase_change"),
    path("<int:pk>/delete/", views.delete, name="purchase_delete"),

    path("returns/", include('purchases.urls_returns')),
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="assets"),
    path("add/", views.add, name="asset_add"),
    path("<int:pk>/", views.detail, name="asset_detail"),
    path("<int:pk>/change/", views.change, name="asset_change"),
    path("<int:pk>/delete/", views.delete, name="asset_delete"),

    path("debtors/", include('assets.urls_debtors')),
]
from django.urls import path, include
from . import views_depreciations as views

urlpatterns = [
    path('', views.index, name="depreciations"),
    path("add/", views.add, name="depreciation_add"),
    path("<int:pk>/", views.detail, name="depreciation_detail"),
    path("<int:pk>/change/", views.change, name="depreciation_change"),
    path("<int:pk>/delete/", views.delete, name="depreciation_delete"),
]

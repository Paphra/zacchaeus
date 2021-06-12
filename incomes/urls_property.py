from django.urls import path, include
from . import views_property as views

urlpatterns = [
    path('', views.index, name="property_incomes"),
    path("add/", views.add, name="property_income_add"),
    path("<int:pk>/", views.detail, name="property_income_detail"),
    path("<int:pk>/change/", views.change, name="property_income_change"),
    path("<int:pk>/delete/", views.delete, name="property_income_delete"),
]

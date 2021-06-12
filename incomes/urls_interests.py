from django.urls import path, include
from . import views_interests as views

urlpatterns = [
    path('', views.index, name="interests"),
    path("add/", views.add, name="interest_add"),
    path("<int:pk>/", views.detail, name="interest_detail"),
    path("<int:pk>/change/", views.change, name="interest_change"),
    path("<int:pk>/delete/", views.delete, name="interest_delete"),
]

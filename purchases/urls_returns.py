from django.urls import path, include
from . import views_returns

urlpatterns = [
    path("", views_returns.index, name="purchases_returns"),
    path("add/", views_returns.add, name="purchases_return_add"),
    path("<int:pk>/", views_returns.detail, name="purchases_return_detail"),
    path("<int:pk>/change/", views_returns.change, name="purchases_return_change"),
    path("<int:pk>/delete/", views_returns.delete, name="purchases_return_delete"),
]

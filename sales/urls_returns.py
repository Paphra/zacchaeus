from django.urls import path, include
from sales import views_returns

urlpatterns = [
    path("", views_returns.index, name="sales_returns"),
    path("add/", views_returns.add, name="sales_return_add"),
    path("<int:pk>/change/", views_returns.change, name="sales_return_change"),
    path("<int:pk>/", views_returns.detail, name="sales_return_detail"),
    path("<int:pk>/delete/", views_returns.delete, name="sales_return_delete"),
]

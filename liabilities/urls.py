from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="liabilities"),
    path("add/", views.add, name="liability_add"),
    path("<int:pk>/", views.detail, name="liability_detail"),
    path("<int:pk>/change/", views.change, name="liability_change"),
    path("<int:pk>/delete/", views.delete, name="liability_delete"),

    path("creditors/", include('liabilities.urls_creditors')),
    path("withdrawals/", include('liabilities.urls_withdrawals')),
]
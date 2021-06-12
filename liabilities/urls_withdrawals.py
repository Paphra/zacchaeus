from django.urls import path, include
from . import views_withdrawals

urlpatterns = [
    path("", views_withdrawals.index, name="withdrawals"),
    path("add/", views_withdrawals.add, name="withdrawal_add"),
    path("<int:pk>/", views_withdrawals.detail, name="withdrawal_detail"),
    path("<int:pk>/change/", views_withdrawals.change, name="withdrawal_change"),
    path("<int:pk>/delete/", views_withdrawals.delete, name="withdrawal_delete"),
]

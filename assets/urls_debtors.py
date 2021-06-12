from django.urls import path, include
from . import views_debtors

urlpatterns = [
    path("", views_debtors.index, name="debtors"),
    path("add/", views_debtors.add, name="debtor_add"),
    path("<int:pk>/", views_debtors.detail, name="debtor_detail"),
    path("<int:pk>/change/", views_debtors.change, name="debtor_change"),
    path("<int:pk>/delete/", views_debtors.delete, name="debtor_delete"),
]

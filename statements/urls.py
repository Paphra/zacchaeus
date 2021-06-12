from django.urls import path
from statements import views

urlpatterns = [
    path("", views.index, name="statements"),
    path("income/", views.income, name="income_statement"),
    path("balance/", views.balance, name="balance_sheet"),
]

from django.urls import path
from statements import views

urlpatterns = [
    path("", views.index, name="statemets"),
    path("balance/", views.balance, name="balance-sheet"),
    path("income/", views.income, name="income-statement"),
]

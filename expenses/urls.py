from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="expenses"),
    path("add/", views.add, name="expense_add"),
    path("<int:pk>/", views.detail, name="expense_detail"),
    path("<int:pk>/change/", views.change, name="expense_change"),
    path("<int:pk>/delete/", views.delete, name="expense_delete"),

    path('depreciations/', include('expenses.urls_depreciations')),
]
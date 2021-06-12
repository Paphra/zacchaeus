from django.urls import path, include
from . import views_creditors

urlpatterns = [
    path("", views_creditors.index, name="creditors"),
    path("add/", views_creditors.add, name="creditor_add"),
    path("<int:pk>/", views_creditors.detail, name="creditor_detail"),
    path("<int:pk>/change/", views_creditors.change, name="creditor_change"),
    path("<int:pk>/delete/", views_creditors.delete, name="creditor_delete"),
]

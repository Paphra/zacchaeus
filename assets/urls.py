from django.urls import path 
from assets import views, views_debtors

urlpatterns = [
    path('', views.index, name="assets"),

    path("debtors/", views_debtors.index, name="debtors"),
]

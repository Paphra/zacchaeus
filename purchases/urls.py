from django.urls import path 
from purchases import views, views_returns

urlpatterns = [
    path('', views.index, name="purchases"),
    path("add/", views.purchase_add, name="purchase_add"),
    path("<int:pk>/change/", views.purchase_change, name="purchase_change"),
    path("<int:pk>/", views.purchase_detail, name="purchase_detail"),
    path("<int:pk>/delete/", views.purchase_delete, name="purchase_delete"),

    # returns
    path("returns/", views_returns.index, name="purchases_returns"),
]
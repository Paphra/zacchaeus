from django.urls import path
from liabilities import views, views_creditors

urlpatterns = [
    path('', views.index, name="liabilities"),

    # creditors
    path("creditors/", views_creditors.index, name="creditors"),
]

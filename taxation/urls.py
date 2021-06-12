from django.urls import path
from taxation import views

urlpatterns = [
    path("", views.index, name="taxation"),
    path("pay-tax", views.pay_tax, name="pay_tax"),
]

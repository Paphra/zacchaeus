from django.urls import path
from incomes import views

urlpatterns = [
    path('', views.index, name="incomes")
]

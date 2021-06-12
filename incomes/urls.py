from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="incomes"),
    path("add/", views.add, name="income_add"),
    path("<int:pk>/", views.detail, name="income_detail"),
    path("<int:pk>/change/", views.change, name="income_change"),
    path("<int:pk>/delete/", views.delete, name="income_delete"),

    path('interests/', include('incomes.urls_interests')),
    path('property/', include('incomes.urls_property')),
]

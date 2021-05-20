from django.urls import path
from taxation import views

urlpatterns = [
    path("", views.index, name="taxation")
]

from django.urls import path
from settings import views

urlpatterns = [
    path("", views.index, name="settings")
]

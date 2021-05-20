from django.urls import path
from mails import views

urlpatterns = [
    path('', views.index, name="mails")
]

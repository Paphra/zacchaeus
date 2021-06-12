from django.urls import path
from policies import views

urlpatterns = [
    path('', views.index, name="policies")
]


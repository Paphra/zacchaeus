from django.urls import path
from mails import views

urlpatterns = [
    path('', views.index, name="mails"),
    path('<int:pk>/delete', views.delete, name="mail_delete"),
    path('<int:pk>/', views.detail, name="mail_detail"),
    path('sent/', views.sent, name="mail_sent"),
    path('compose/', views.compose, name="mail_compose"),
]

from django.urls import path

from dashboard import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),
]
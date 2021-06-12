from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="stock"),
    path('closing/', include('stock.urls_closing')),
    path('opening/', include('stock.urls_opening')),
]

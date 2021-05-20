"""zacchaeus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static

from django_registration.backends.activation.views import RegistrationView
from businesses.forms import UserForm

from . import settings

admin.site.site_header = settings.COMPANY_FULL
admin.site.site_title = settings.COMPANY
# admin.site.site_url = None
# admin.site.index_title = "Admin | " + settings.COMPANY

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',
            RegistrationView.as_view(
                form_class=UserForm
            ),
            name='django_registration_register',
        ),
    path('', include('django_registration.backends.activation.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('dashboard.urls')),

    path('assets/', include('assets.urls')),
    path('business/', include('businesses.urls')),
    path("charts/", include('charts.urls')),
    path('contact-us/', include('contact.urls')),
    path('expenses/', include('expenses.urls')),
    path('faq/', include('faq.urls')),
    path('incomes/', include('incomes.urls')),
    path('liabilities/', include('liabilities.urls')),
    path('mails/', include('mails.urls')),
    path('policies/', include('policies.urls')),
    path('purchases/', include('purchases.urls')),
    path('sales/', include('sales.urls')),
    path('settings/', include('settings.urls')),
    path('statements/', include('statements.urls')),
    path('stock/', include('stock.urls')),
    path('taxation/', include('taxation.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
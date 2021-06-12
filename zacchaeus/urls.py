from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static

from django_registration.backends.activation.views import RegistrationView
from persons.forms import UserForm

from . import settings

admin.site.site_header = settings.COMPANY_FULL
admin.site.site_title = settings.COMPANY

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
    path('persons/', include('persons.urls')),
    path('sales/', include('sales.urls')),
    path('expenses/', include('expenses.urls')),
    path('purchases/', include('purchases.urls')),
    path('assets/', include('assets.urls')),
    path('liabilities/', include('liabilities.urls')),
    path('charts/', include('charts.urls')),
    path('contacts/', include('contact.urls')),
    path('faq/', include('faq.urls')),
    path('incomes/', include('incomes.urls')),
    path('mails/', include('mails.urls')),
    path('policies/', include('policies.urls')),
    path('statements/', include('statements.urls')),
    path('stocks/', include('stock.urls')),
    path('taxation/', include('taxation.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

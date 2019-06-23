"""
This urlconf exists so we can run tests without an actual
Django project (Django expects ROOT_URLCONF to exist.)

It is not used by installed instances of this app.
"""
import django

if django.get_version()[0] == '2':
    from django.urls import include, path
else:
    from django.conf.urls import include, url as path

urlpatterns = [
    path("invoices/", include("faktura.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
]

import django

from .views import (
    InvoiceListView,
    InvoiceYearArchiveView,
    InvoiceDetailView,
    InvoiceDetailPDFView,
)

if django.get_version()[0] == '2':
    from django.urls import path
else:
    from django.conf.urls import url as path


urlpatterns = [
    path("<uuid:pk>/download/", InvoiceDetailPDFView.as_view(), name="pdf"),
    path("<uuid:pk>/", InvoiceDetailView.as_view(), name="detail"),
    path("<int:year>/", InvoiceYearArchiveView.as_view(), name="year_archive"),
    path("", InvoiceListView.as_view(), name="list"),
]

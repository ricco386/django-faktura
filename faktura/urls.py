from django.urls import path
from .views import (
    InvoiceListView,
    InvoiceYearArchiveView,
    InvoiceDetailView,
    InvoiceDetailPDFView,
)


urlpatterns = [
    path("<uuid:pk>/download/", InvoiceDetailPDFView.as_view(), name="pdf"),
    path("<uuid:pk>/", InvoiceDetailView.as_view(), name="detail"),
    path("<int:year>/", InvoiceYearArchiveView.as_view(), name="year_archive"),
    path("", InvoiceListView.as_view(), name="list"),
]

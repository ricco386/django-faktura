import logging

from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from subprocess import CalledProcessError
from wkhtmltopdf.views import PDFTemplateResponse

from .models import Invoice
from .utils import get_invoice_years

logger = logging.getLogger(__name__)


class InvoiceListView(ListView):
    model = Invoice
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["invoice_years"] = get_invoice_years()

        return context


class InvoiceYearArchiveView(YearArchiveView):
    queryset = Invoice.objects.all()
    date_field = "date_of_issue"
    make_object_list = True
    allow_future = True
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["invoice_years"] = get_invoice_years()

        return context


class InvoiceDetailView(DetailView):
    model = Invoice

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["invoice_years"] = get_invoice_years()
        context["generating_pdf"] = False

        return context


class InvoiceDetailPDFView(InvoiceDetailView):
    template_name = "faktura/invoice_detail.html"
    model = Invoice

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["generating_pdf"] = True

        return context

    def render_to_response(self, context):
        try:
            response = PDFTemplateResponse(
                request=self.request,
                template=self.template_name,
                filename="invoice-%s.pdf" % self.object.number,
                context=self.get_context_data(),
                show_content_in_browser=False,
                cmd_options={
                    "page-size": "A4",
                    "no-stop-slow-scripts": True,
                    "dpi": 300,
                    "margin-bottom": 3,
                    "margin-top": 3,
                    "margin-left": 0,
                    "margin-right": 0,
                    "encoding": "utf8",
                },
            )
        except CalledProcessError as e:
            logger.critical("Generating PDF raised an exception: %s", e)
            messages.error(
                self.request, _("Generating PDF failed. Please try again later.")
            )

            return redirect("detail", order_id=self.object.id)

        return response

from django.core.management.base import BaseCommand, CommandError
from faktura.models import Invoice
from faktura.utils import generate_invoice


class Command(BaseCommand):
    help = "Generate Invoice (in DRAFT state) from existing pro forma invoice."

    def add_arguments(self, parser):
        parser.add_argument("proforma_invoices", nargs="+", type=str)

    def handle(self, *args, **options):
        for pk in options["proforma_invoices"]:
            try:
                proforma_invoice = Invoice.objects.get(pk=pk)
            except Invoice.DoesNotExist:
                raise CommandError('Invoice with ID: "%s" does not exist!' % pk)

            try:
                generate_invoice(proforma_invoice)
            except ValueError as e:
                raise CommandError(e)

            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully created NEW invoice (in DRAFT state) for existing "
                    "pro forma invoice."
                )
            )

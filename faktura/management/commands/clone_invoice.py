from django.core.management.base import BaseCommand, CommandError
from faktura.models import Invoice
from faktura.utils import clone_invoice


class Command(BaseCommand):
    help = "Clone Invoice (in DRAFT state) from existing invoice (any type)."

    def add_arguments(self, parser):
        parser.add_argument("invoices", nargs="+", type=str)

    def handle(self, *args, **options):
        for pk in options["invoices"]:
            try:
                invoice = Invoice.objects.get(pk=pk)
            except Invoice.DoesNotExist:
                raise CommandError('Invoice with ID: "%s" does not exist!' % pk)

            try:
                clone_invoice(invoice)
            except ValueError as e:
                raise CommandError(e)

            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully created NEW invoice (in DRAFT state) for existing "
                    "invoice."
                )
            )

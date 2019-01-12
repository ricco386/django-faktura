import datetime

from .models import Invoice


def clone_invoice(invoice):
    """
    Create a clone of selected invoice and save it as a draft.

    :param invoice:
    :return: Newly cloned invoice (draft)
    """
    items = invoice.items.all()

    invoice.pk = None
    invoice.number = None
    invoice.status = Invoice.DRAFT
    invoice.invoice = None
    invoice.save()

    for item in items:
        item.pk = None
        item.invoice = invoice
        item.save()

    return invoice


def generate_invoice(proforma_invoice):
    """
    Generate an invoice from pro forma invoice or credit note and save it as a draft.

    :param proforma_invoice:
    :return: Newly generated invoice for pro forma invoice (draft)
    """
    if proforma_invoice.type == Invoice.INVOICE:
        raise ValueError(
            "It is not possible to generate invoice from invoice! Provide pro forma invoice or credit "
            "note."
        )

    invoice = clone_invoice(proforma_invoice)
    invoice.date_of_issue = datetime.datetime.now()
    invoice.due_date = datetime.datetime.now()
    invoice.type = Invoice.INVOICE
    invoice.save()

    proforma_invoice.invoice = invoice
    proforma_invoice.save()

    return invoice


def get_invoice_years():
    invoice_years = []

    for entry in Invoice.objects.all():
        if entry.date_of_issue.year not in invoice_years:
            invoice_years.append(entry.date_of_issue.year)

    return invoice_years

import pytest
import datetime

from faktura.models import Invoice, Item


@pytest.mark.django_db
def test_invoice_items_counts_save(django_user_model):
    john_doe = django_user_model.objects.create_user(
        "johndoe", email="jd@example.com", password="123456"
    )
    i = Invoice(
        seller="XYZ",
        seller_details="Data about XYZ",
        buyer="ABC",
        buyer_details="Data about ABC",
        author=john_doe,
    )
    i.save()

    PRICE = 100
    QUANTITY = (1, 2, 3)

    for X in QUANTITY:
        ii = Item(invoice=i, title="Test", price=PRICE, quantity=X)
        ii.save()
        assert ii.total_amount == PRICE * X

    assert i.seller == "XYZ"
    assert i.items_total == 600  # 1*100 + 2*100 + 3*100


@pytest.mark.django_db
def test_invoice_status_save(django_user_model):
    current_year = datetime.datetime.now().year
    john_doe = django_user_model.objects.create_user(
        "johndoe", email="jd@example.com", password="123456"
    )
    i = Invoice(
        seller="XYZ",
        seller_details="Data about XYZ",
        buyer="ABC",
        buyer_details="Data about ABC",
        author=john_doe,
        status=Invoice.DRAFT,
    )
    i.save()
    i2 = Invoice(
        seller="XYZ",
        seller_details="Data about XYZ",
        buyer="ABC",
        buyer_details="Data about ABC",
        author=john_doe,
        status=Invoice.FINAL,
    )
    i2.save()
    assert i.number is None  # Storing as a draft does note generate invoice number
    assert i2.number == f"001/{current_year}"  # Default format for invoice number generation

    i.status = Invoice.FINAL
    i.save()
    assert i.number == f"002/{current_year}"  # Invoice was changed from DRAFT to FINAL, number has been generated.

    i3 = Invoice(
        seller="XYZ",
        seller_details="Data about XYZ",
        buyer="ABC",
        buyer_details="Data about ABC",
        author=john_doe,
        type=Invoice.PROFORMA,
        status=Invoice.FINAL,
    )
    i3.save()
    assert i3.number == f"P001/{current_year}"

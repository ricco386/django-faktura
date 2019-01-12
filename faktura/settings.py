from django.conf import settings


DEFAULT_DUE_DATE = getattr(settings, "DEFAULT_DUE_DATE", 14)
DEFAULT_STATUS = getattr(settings, "DEFAULT_STATUS", "draft")
DEFAULT_TYPE = getattr(settings, "DEFAULT_TYPE", "invoice")

DEFAULT_SELLER = getattr(settings, "DEFAULT_SELLER", None)
DEFAULT_SELLER_DETAILS = getattr(settings, "DEFAULT_SELLER_DETAILS", None)

DEFAULT_BUYER = getattr(settings, "DEFAULT_BUYER", None)
DEFAULT_BUYER_DETAILS = getattr(settings, "DEFAULT_BUYER_DETAILS", None)

DEFAULT_INCLUDES_VAT = getattr(settings, "DEFAULT_INCLUDES_VAT", False)
DEFAULT_VAT = getattr(settings, "DEFAULT_VAT", 0)
DEFAULT_CURRENCY = getattr(settings, "DEFAULT_CURRENCY", "EUR")
DEFAULT_DISCOUNT = getattr(settings, "DEFAULT_DISCOUNT", 0)

DEFAULT_NOTE = getattr(settings, "DEFAULT_NOTE", None)

DEFAULT_ITEM_QUANTITY = getattr(settings, "DEFAULT_ITEM_QUANTITY", 1)

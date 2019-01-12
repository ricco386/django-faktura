from django.contrib import admin
from django.utils.translation import gettext as _

from .models import Invoice, Item
from .settings import DEFAULT_SELLER, DEFAULT_SELLER_DETAILS, DEFAULT_NOTE
from .utils import clone_invoice


def make_invoices_final(modeladmin, request, queryset):
    queryset.update(status=Invoice.FINAL)


def clone_invoices(modeladmin, request, queryset):
    for invoice in queryset.all():
        clone_invoice(invoice)


def generate_invoices(modeladmin, request, queryset):
    for invoice in queryset.all():
        clone_invoice(invoice)


make_invoices_final.short_description = _("Mark selected Invoices as final document")
clone_invoices.short_description = _("Clone selected Invoices (save as drafts)")
generate_invoices.short_description = _(
    "Generate Invoices for selected pro forma Invoices"
)

# Globally disable delete selected
admin.site.disable_action("delete_selected")


class ItemInlineAdmin(admin.TabularInline):
    model = Item
    extra = 1

    def has_delete_permission(self, request, obj=None):
        if obj and obj.status == Invoice.FINAL:
            return False

        return super().has_delete_permission(request, obj)

    def has_add_permission(self, request, obj=None):
        if obj and obj.status == Invoice.FINAL:
            return False

        return super().has_add_permission(request, obj)

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status == Invoice.FINAL:
            self.extra = 0
            self.can_delete = False

            return "title", "price", "quantity"

        return self.readonly_fields


@admin.register(Invoice)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "type",
        "date_of_issue",
        "due_date",
        "buyer",
        "get_status_display",
        "total_amount",
        "currency",
        "includes_vat",
    )
    search_fields = ("buyer",)
    list_filter = ("type", "status", "due_date", "currency", "includes_vat")
    ordering = ("-due_date", "-number")
    readonly_fields = ("id", "created_at", "updated_at")
    fieldsets = (
        (
            _("Invoice details"),
            {"fields": ("number", "date_of_issue", "due_date", "type", "status")},
        ),
        (_("Buyer"), {"fields": ("buyer", "buyer_details")}),
        (
            _("Seller"),
            {"fields": ("seller", "seller_details"), "classes": ("collapse",)},
        ),
        (
            _("Invoice state"),
            {
                "fields": (
                    "invoice",
                    "includes_vat",
                    "vat",
                    "currency",
                    "discount",
                    "note",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            _("Modifications"),
            {
                "fields": ("author", "created_at", "updated_at", "id"),
                "classes": ("collapse",),
            },
        ),
    )
    inlines = (ItemInlineAdmin,)
    actions = (make_invoices_final, clone_invoices)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.status == Invoice.FINAL:
            return False

        return super().has_delete_permission(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if obj is None or obj and obj.status != Invoice.FINAL:
            form.base_fields["seller"].initial = DEFAULT_SELLER
            form.base_fields["seller_details"].initial = DEFAULT_SELLER_DETAILS
            form.base_fields["note"].initial = DEFAULT_NOTE
            form.base_fields["author"].initial = request.user

        return form

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)

        if obj and obj.status == Invoice.FINAL:
            for fieldset in fieldsets:
                if "classes" in fieldset[1]:
                    del (fieldset[1]["classes"])

        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status == Invoice.FINAL:
            return self.readonly_fields + (
                "number",
                "type",
                "date_of_issue",
                "due_date",
                "buyer",
                "buyer_details",
                "seller",
                "seller_details",
                "type",
                "currency",
                "note",
                "items",
                "discount",
                "vat",
                "includes_vat",
                "invoice",
                "author",
            )

        return self.readonly_fields

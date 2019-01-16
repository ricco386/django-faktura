def add_permissions_to_group(group_name, permissions):
    from django.contrib.auth.models import Group

    group_object, created = Group.objects.get_or_create(name=group_name)
    group_object.permissions.add(*permissions)


def populate_models(sender, **kwargs):
    from django.apps import apps
    from .apps import FakturaConfig
    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType
    from django.db.models import Q

    for model in apps.all_models[FakturaConfig.name]:
        content_type = ContentType.objects.get(
            app_label=FakturaConfig.name, model=model
        )

        add_permissions_to_group(
            "Invoicing managers", Permission.objects.filter(content_type=content_type)
        )

    add_permissions_to_group(
        "Invoicing observers",
        Permission.objects.filter(Q(codename="view_invoice") | Q(codename="view_item")),
    )

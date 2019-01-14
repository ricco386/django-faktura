def populate_models(sender, **kwargs):
    from django.apps import apps
    from .apps import FakturaConfig
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from django.db.models import Q

    group_managers, created = Group.objects.get_or_create(name="Invoicing managers")
    models = apps.all_models[FakturaConfig.name]

    for model in models:
        content_type = ContentType.objects.get(
            app_label=FakturaConfig.name, model=model
        )
        permissions = Permission.objects.filter(content_type=content_type)
        group_managers.permissions.add(*permissions)

    group_observers, created = Group.objects.get_or_create(name="Invoicing observers")
    permissions = Permission.objects.filter(
        Q(codename="view_invoice") | Q(codename="view_item")
    )
    group_observers.permissions.add(*permissions)

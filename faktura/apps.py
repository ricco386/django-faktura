from django.apps import AppConfig
from django.db.models.signals import post_migrate

from .signals import populate_models


class FakturaConfig(AppConfig):
    name = "faktura"

    def ready(self):
        post_migrate.connect(populate_models, sender=self)

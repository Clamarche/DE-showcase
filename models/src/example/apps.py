"""Example app config."""

from django.apps import AppConfig  # type: ignore


class ExampleConfig(AppConfig):
    """Example app config."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "models.src.example"

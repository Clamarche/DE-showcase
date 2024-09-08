"""Example admin."""

from django.contrib import admin  # type: ignore

from models.src.example.models import Example


# Register your models here.
@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    """Example admin."""

    list_display = (
        "name",
        "email",
        "birthdate",
        "last_updated",
        "wants_notifications",
    )

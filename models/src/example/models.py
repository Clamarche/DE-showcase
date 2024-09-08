"""Django models for example model."""

from django.db import models  # type: ignore
from django_extensions.db.models import TimeStampedModel  # type: ignore

from models.src.utils.basemodel import BaseModel


# Create your models here.
class Example(TimeStampedModel, BaseModel):
    """Example model."""

    class Meta:
        """Meta class."""
        app_label = "example"
        verbose_name = "Example"
        verbose_name_plural = "Examples"

    name = models.CharField(max_length=255)
    email = models.EmailField()
    birthdate = models.DateField()
    last_updated = models.DateTimeField(auto_now=True)
    wants_notifications = models.BooleanField(default=True)


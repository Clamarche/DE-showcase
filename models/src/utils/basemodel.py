"""Base model."""

import uuid

from django.db import models  # type: ignore


class BaseModel(models.Model):
    """Base model."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        """Meta class."""
        abstract = True

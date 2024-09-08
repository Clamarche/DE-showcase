"""Example serializers."""

from rest_framework import serializers

from models.src.example import models


class ExampleSerializer(serializers.ModelSerializer):
    """Example serializer."""

    class Meta:
        """Meta class."""
        model = models.Example
        fields = (
            "name",
            "email",
            "birthdate",
            "last_updated",
            "wants_notifications",
        )

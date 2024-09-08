"""Example views."""

from rest_framework import status, viewsets
from rest_framework.response import Response

from models.src.example import models
from models.src.example.serializers import ExampleSerializer


# Create your views here.
class ExampleView(viewsets.ModelViewSet):
    """Example view."""

    serializer_class = ExampleSerializer
    queryset = models.Example.objects.all()

    def get_serializer_context(self) -> dict:
        """Get serializer context."""
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    def get_serializer(self, *args, **kwargs) -> ExampleSerializer:
        """Get serializer."""
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, format=None, *args, **kwargs) -> Response:
        """Create an example from a POST request."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

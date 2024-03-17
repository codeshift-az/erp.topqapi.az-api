from rest_framework import serializers

import server.apps.staff.logic.schema  # noqa: F401
from server.apps.staff.logic.serializers import DriverSerializer, SellerSerializer, WorkerSerializer
from server.apps.staff.models import Driver, Seller, Worker


class DriverField(serializers.RelatedField):
    """Serializer definition for Driver field."""

    def get_queryset(self):
        """Return queryset of Driver objects."""
        return Driver.objects.all()

    def to_representation(self, value: Driver) -> dict:
        """Return representation of Driver object."""
        return DriverSerializer(value).data

    def to_internal_value(self, data: int) -> Driver:
        """Return Driver object from given data."""
        driver = Driver.objects.get(pk=data)

        if driver is None:
            return serializers.ValidationError(f"Driver with id {data} does not exist.")

        return driver


class SellerField(serializers.RelatedField):
    """Serializer definition for Seller field."""

    def get_queryset(self):
        """Return queryset of Seller objects."""
        return Seller.objects.all()

    def to_representation(self, value: Seller) -> dict:
        """Return representation of Seller object."""
        return SellerSerializer(value).data

    def to_internal_value(self, data: int) -> Seller:
        """Return Seller object from given data."""
        seller = Seller.objects.get(pk=data)

        if seller is None:
            return serializers.ValidationError(f"Seller with id {data} does not exist.")

        return seller


class WorkerField(serializers.RelatedField):
    """Serializer definition for Worker field."""

    def get_queryset(self):
        """Return queryset of Worker objects."""
        return Worker.objects.all()

    def to_representation(self, value: Worker) -> dict:
        """Return representation of Worker object."""
        return WorkerSerializer(value).data

    def to_internal_value(self, data: int) -> Worker:
        """Return Worker object from given data."""
        worker = Worker.objects.get(pk=data)

        if worker is None:
            return serializers.ValidationError(f"Worker with id {data} does not exist.")

        return worker

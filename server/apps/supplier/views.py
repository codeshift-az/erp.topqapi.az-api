from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Core
from server.apps.core.logic import responses

# Supplier
from server.apps.supplier.logic.filters import SupplierFilter
from server.apps.supplier.logic.serializers import SupplierSerializer, SupplierTransactionSerializer
from server.apps.supplier.models import Supplier


class SupplierViewSet(viewsets.ModelViewSet):
    """Viewset for Supplier model."""

    queryset = Supplier.objects.none()
    serializer_class = SupplierSerializer

    filterset_class = SupplierFilter
    ordering_fields = "__all__"

    verbose_name = "supplier"
    verbose_name_plural = "suppliers"

    lookup_field = "id"

    def get_queryset(self):
        """Get the queryset for SupplierViewSet."""
        return Supplier.objects.get_related().get_debt()

    @extend_schema(
        description="Retrieve list of all transactions of the supplier.",
        responses={
            status.HTTP_200_OK: SupplierTransactionSerializer,
            status.HTTP_401_UNAUTHORIZED: responses.UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: responses.FORBIDDEN,
        },
    )
    @action(detail=True, methods=["get"])
    def transactions(self, request, *args, **kwargs):
        supplier = self.get_object()

        if not supplier:
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset = supplier.get_transactions()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = SupplierTransactionSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SupplierTransactionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        description=f"Retrieve list of all {verbose_name_plural}.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_401_UNAUTHORIZED: responses.UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: responses.FORBIDDEN,
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description=f"Retrieve a {verbose_name} by {lookup_field}.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_401_UNAUTHORIZED: responses.UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: responses.FORBIDDEN,
            status.HTTP_404_NOT_FOUND: responses.NOT_FOUND,
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description=f"Create a new {verbose_name}.",
        responses={
            status.HTTP_201_CREATED: serializer_class,
            status.HTTP_400_BAD_REQUEST: responses.BAD_REQUEST,
            status.HTTP_401_UNAUTHORIZED: responses.UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: responses.FORBIDDEN,
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        description=f"Update an existing {verbose_name} by {lookup_field}.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_401_UNAUTHORIZED: responses.UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: responses.FORBIDDEN,
            status.HTTP_404_NOT_FOUND: responses.NOT_FOUND,
        },
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        description=f"Partially update an existing {verbose_name} by {lookup_field}.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_401_UNAUTHORIZED: responses.UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: responses.FORBIDDEN,
            status.HTTP_404_NOT_FOUND: responses.NOT_FOUND,
        },
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description=f"Delete an existing {verbose_name} by {lookup_field}.",
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: responses.UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: responses.FORBIDDEN,
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

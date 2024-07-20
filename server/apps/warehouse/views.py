from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Core
from server.apps.core.logic import responses

# Warehouse
from server.apps.warehouse.logic.filters import WarehouseEntryFilter, WarehouseItemFilter
from server.apps.warehouse.logic.serializers import (
    WarehouseCartItemSerializer,
    WarehouseEntrySerializer,
    WarehouseItemSerializer,
    WarehouseProductSerializer,
)
from server.apps.warehouse.models import WarehouseCartItem, WarehouseEntry, WarehouseItem


class WarehouseEntryViewSet(viewsets.ModelViewSet):
    """Viewset for WarehouseEntry model."""

    queryset = WarehouseEntry.objects.none()
    serializer_class = WarehouseEntrySerializer

    filterset_class = WarehouseEntryFilter
    ordering_fields = "__all__"

    verbose_name = "entry to warehouse"
    verbose_name_plural = "entries to warehouse"

    lookup_field = "id"

    def get_queryset(self):
        """Get the queryset for this view."""
        return (
            WarehouseEntry.objects.select_related(
                "supplier",
            )
            .prefetch_related(
                "items",
                "items__product",
                "items__product__category",
            )
            .all()
        )

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


class WarehouseItemViewSet(viewsets.ModelViewSet):
    """Viewset for WarehouseItem model."""

    queryset = WarehouseItem.objects.none()
    serializer_class = WarehouseItemSerializer

    filterset_class = WarehouseItemFilter
    ordering_fields = "__all__"

    verbose_name = "item in warehouse"
    verbose_name_plural = "items in warehouse"

    lookup_field = "id"

    def get_queryset(self):
        """Get the queryset for this view."""
        return WarehouseItem.objects.get_related().get_sales()

    @extend_schema(
        description="Retrieve stats of all items in warehouse.",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="WarehouseItemStats",
                fields={
                    "total_quantity": int,
                    "total_sales": int,
                    "total_left": int,
                    "total_investment_left": float,
                },
            ),
            status.HTTP_401_UNAUTHORIZED: responses.UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: responses.FORBIDDEN,
        },
    )
    @action(methods=["GET"], detail=False, url_path="stats/all", url_name="stats_all")
    def stats_all(self, request, *args, **kwargs):
        queryset = self.filter_queryset(queryset=WarehouseItem.objects.get_related())

        stats = queryset.get_stats()

        return Response(stats, status=status.HTTP_200_OK)

    @extend_schema(
        description="Retrieve list of all products in warehouse with stats.",
        responses={
            status.HTTP_200_OK: WarehouseProductSerializer(many=True),
            status.HTTP_401_UNAUTHORIZED: responses.UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: responses.FORBIDDEN,
        },
    )
    @action(methods=["GET"], detail=False, url_name="stats")
    def stats(self, request, *args, **kwargs):
        queryset = self.filter_queryset(queryset=WarehouseItem.objects.get_related())

        queryset = queryset.get_product_stats()

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = WarehouseProductSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = WarehouseProductSerializer(queryset, many=True)
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


class WarehouseCartItemViewSet(viewsets.ModelViewSet):
    """Viewset for WarehouseCartItem model."""

    queryset = WarehouseCartItem.objects.none()
    serializer_class = WarehouseCartItemSerializer

    pagination_class = None

    verbose_name = "item in warehouse cart"
    verbose_name_plural = "items in warehouse cart"

    lookup_field = "id"

    def get_queryset(self):
        """Get the queryset for this view."""
        return WarehouseCartItem.objects.select_related(
            "product",
            "product__category",
        ).filter(user=self.request.user)

    @extend_schema(
        description=f"Retrieve list of all {verbose_name_plural}s.",
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

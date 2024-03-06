from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets

# Core
from server.apps.core.logic import responses

# Product
from server.apps.warehouse.logic.filters import EntryFilter, ProductFilter
from server.apps.warehouse.logic.serializers import EntrySerializer, ProductSerializer
from server.apps.warehouse.models import Entry, Product


class EntryViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset for Entry model."""

    queryset = (
        Entry.objects.all()
        .select_related(
            "supplier",
        )
        .prefetch_related("products", "products__product", "products__product__category")
    )
    serializer_class = EntrySerializer

    filterset_class = EntryFilter
    search_fields = (
        "supplier__name",
        "invoice",
    )
    ordering_fields = "__all__"

    verbose_name = "entry to warehouse"
    verbose_name_plural = "entries to warehouse"

    lookup_field = "id"

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


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset for Product model."""

    queryset = Product.objects.all().select_related("product", "product__category")
    serializer_class = ProductSerializer

    filterset_class = ProductFilter
    search_fields = (
        "product__name",
        "product__category__name",
    )
    ordering_fields = "__all__"

    verbose_name = "product in warehouse"
    verbose_name_plural = "products in warehouse"

    lookup_field = "id"

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

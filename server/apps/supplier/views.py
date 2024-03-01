from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets

# Core
from server.apps.core.logic.responses import BAD_REQUEST, FORBIDDEN, NOT_FOUND, UNAUTHORIZED

# Supplier
from server.apps.supplier.logic.filters import SupplierFilter
from server.apps.supplier.logic.serializers import SupplierSerializer
from server.apps.supplier.models import Supplier


class SupplierViewSet(viewsets.ModelViewSet):
    """Viewset for Supplier model."""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    filterset_class = SupplierFilter
    search_fields = ("name",)
    ordering_fields = "__all__"

    verbose_name = "supplier"
    verbose_name_plural = "suppliers"

    lookup_field = "id"

    @extend_schema(
        description=f"Retrieve list of all {verbose_name_plural}s.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description=f"Retrieve a {verbose_name} by {lookup_field}.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
            status.HTTP_404_NOT_FOUND: NOT_FOUND,
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description=f"Create a new {verbose_name}.",
        responses={
            status.HTTP_201_CREATED: serializer_class,
            status.HTTP_400_BAD_REQUEST: BAD_REQUEST,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        description=f"Update an existing {verbose_name} by {lookup_field}.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
            status.HTTP_404_NOT_FOUND: NOT_FOUND,
        },
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        description=f"Partially update an existing {verbose_name} by {lookup_field}.",
        responses={
            status.HTTP_200_OK: serializer_class,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
            status.HTTP_404_NOT_FOUND: NOT_FOUND,
        },
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description=f"Delete an existing {verbose_name} by {lookup_field}.",
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED,
            status.HTTP_403_FORBIDDEN: FORBIDDEN,
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
